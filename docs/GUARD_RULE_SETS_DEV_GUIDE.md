# Developing Managed Rule Sets

[AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) allows for organizations and groups to create multiple rule files and categorize them as a single `rule set` so that you can validate your JSON- or YAML-formatted data against a single source. The AWS Guard Rules Registry provides provides a process to automatically map and build these rule sets against its centralized repository of Guard rule files.

## How to Contribute

To start developing your own Guard Registry Rule Set start by forking this repository. Once you have forked the repo, follow the [Guard Rules Development Guide](./GUARD_RULES_DEV_GUIDE.md) to create any necessary custom rules. Creating custom rules is not required to start with your own custom rule set within the registry. You can simply identify the rules you want to use within the repo and document what controls those individual rules will fulfill for your compliance framework. Next follow the steps in the [Using Guard Map](#using-guard-map) section of the guide below.

> **Important:** All custom rule set contributions are listed here publicly and available for use by the public. **Do not put anything sensitive in nature in your contributions.** The AWS Guard Rules Registry can be refactored for your own private use; however, maintaining the build pipeline is on the end-users responsibility.

# Using Guard Map

Guard Map is the process of creating a Guard Rule Sets by mapping individual Guard Rule Files to your compliance framework and list of controls. Contributors can submit [Pull Requests](../CONTRIBUTING.md/#contributing-via-pull) containing a Guard Map file that upon build time will generate a Guard Rule Registry Rule Set made available in the release and the supported docker image build.

AWS Guard Rule Registry supports a pipeline through GitHub Actions that facilitates a Guard rule test and compilation of Managed Rule Set files based on mapping files located in the [mappings](/mappings) directory. Follow these steps to create a custom AWS Guard Rules Registry Rule Set:

1. Within the [./mappings/](../mappings/) directory create a .json file with the prefix `rule_set_` and the name of your aws rule set (use snake casing with all lowercase)
2. Edit your mapping JSON file creating a JSON structure detailed in the [Rule Set Mapping File](#rule-set-mapping-file) section below. Create as many mapping list elements as your compliance framework requires
3. Validate your information within the mappings JSON file ensuring all required information is set or updated.
4. Review the [Pull Request Checklist](../CONTRIBUTING.md/#pull-request-checklist)
5. Submit a [Pull Request](../CONTRIBUTING.md/#contributing-via-pull)

## Rule Set Mapping File

The `mappings` directory holds rule set JSON files that describe control mappings between a standard or framework and rules in the registry. **All Guard Map files are required to be prefixed with `rule_set_` and are built whenever a merge to the main branch happens.**

| **Attribute** | **Description** |
| ------------: | :-------------- |
| `owner` | the rule set owner (`required`) |
| `ruleSetName` | Name of the rule set that will be generated as a guard rule file and available. The name will be displayed in the custom message for all associated mappings. (`required`) |
| ` version` | current version of the guard rule set (`required`) |
| `description` | Description of what the guard rule set or compliance framework (`required`) |
| `contact` | primary point of contact for the rule set. This can be github user or email. Preference is github user to contact unless organization requires multiple contacts. (`required`) |
| `mappings` | a list of guard file path and the controls the guard file path will be mapped to. (`required`) |
| `guardFilePath` | the file path of the guard file (rule) you want to add to your rule set. (`required`) |
| `controls` | a list of your compliance controls you want mapped to the guard rule. This list will be aggregated and displayed in the custom message. (`optional`) |

The following is an example of a Guard Map file.

> **Dev Note:** The `controls` list is optional and if not used will still need to be present. To do this leave the list empty such as `"controls": []`.

```json
{
  "owner": "example.com",
  "ruleSetName": "example-framework",
  "version": "1.0.0",
  "description" : "example.com CCOE compliance framework",
  "contact" : "grolston",
  "mappings": [
    {
      "guardFilePath": "rules/aws/amazon_s3/s3_bucket_version_enabled.guard",
      "controls": [
        "CCOE-Sec-1.0",
        "CCOE-DR-2.1"
      ]
    },
    {
      "guardFilePath": "rules/aws/amazon_ec2/ec2_ebs_encryption_by_default.guard",
      "controls": [
        "CCOE-Sec-1.1",
        "DAR-1.0"
      ]
    }
  ]
}
```

