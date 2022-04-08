function new-ruleset ($BuildName, $Owner, $BuildVersion) {
  $BuildDate = $(Get-Date).ToShortDateString()
  $RuleSetStr = @"
################################################################
## Name: $BuildName
## Owner: $Owner
## Build Version: $BuildVersion
## Build Date: $BuildDate
################################################################
"@
return $RuleSetStr
}
function new-custommessage($ControlList, $ComplianceFramework){
  $custommessagestr = @"
<<
    Compliance Framework: $ComplianceFramework
    Controls: $ControlList
"@
return $custommessagestr
}
function build-me {
$RuleSetBuilds = Get-ChildItem -Path ./build/rule_set_* -File:$true -Directory:$false

foreach ($RuleSetBuild in $RuleSetBuilds){

  $BuildDetails = Get-Content ./build/$($RuleSetBuild.Name) | ConvertFrom-Json -Depth 10
  $ComplianceFramework = $BuildDetails.RuleSetName
  $NewRuleSetStr = new-ruleset -BuildName $BuildDetails.RuleSetName -Owner $BuildDetails.Owner -BuildVersion $BuildDetails.BuildVersion
  foreach($GuardRule in $BuildDetails.Rules){
    $GuardRuleFile = $GuardRule.CfnGuardFile
    try{
    $FileContents = Get-Content -Raw -Path ./$GuardRuleFile -ErrorAction Stop
    }catch{
      write-host "missing $GuardRuleFile"
    }
    if($FileContents.StartsWith('## SKIP')) {
      write-host "skipping $GuardRuleFile"
    }else{
      ## Temporary Logic to ensure file has a rule with correct message
      if($FileContents.Contains("<<")){
        ## put the controls list into single line separated by commas for readability
        $ControlList = $GuardRule.Controls -join ","
        ## create custom message to prefix the guard rule custom message
        $custommessageprefix = new-custommessage -ControlList $ControlList -ComplianceFramework $ComplianceFramework
        $NewRuleSetStr += "`r`n"
        ## add Guard Rule block to string
        $NewRuleSetStr += $FileContents.Replace("<<", $custommessageprefix)
      }#end if rule check
    }
  }#end foreach GuardRule
  Out-File ./build/output/$($BuildDetails.RuleSetName).guard -InputObject $NewRuleSetStr
}#end foreach Ruleset

}

build-me