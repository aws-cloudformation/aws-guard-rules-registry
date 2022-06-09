# Using Guard Map

Guard Map is the process of creating a Guard Rule Sets by mapping individual guard rule files to compliance framework controls. Contributors can submit Pull Requests containing a Guard Map file that upon build time will generate a Guard Rule Registry Rule Set made available in the release and the supported docker image build.


AWS Guard Rule Registry supports a pipeline through GitHub Actions that facilitates a guard rule test and compilation of Managed Rule Set files based on mapping files located in the [mappings](/mappings) directory.

## Rule Set Mapping Files

The `mappings` directory holds rule set documents that describe control mappings between a standard or framework and rules in the registry. All Guard Map files are prefixed with `rule_set_` and are built whenever a merge to the main branch happens.

| **Attribute** | **Description** |
| ------------: | --------------- |
| `owner` | the rule set owner |
| `ruleSetName` | Name of the rule set that will be generated as a guard rule file and available |
| ` version` | current version of the guard rule set |
| `description` | Description of what the guard rule set or compliance framework |
| `contact` | primary point of contact for the rule set. This can be github user or email. |
| `mappings` | a list of guard file path and the controls the guard file path will be mapped to. |

The following is an example of a Guard Map file.

```json
{
  "owner": "AWS",
  "ruleSetName": "NIST800-53Rev4",
  "version": "0.1.0",
  "description" : "AWS Guard rule set based on the AWS Config Conformance Pack for NIST 800-53 revision 4.",
  "contact" : "aws-guard-rules-registry@amazon.com",
  "mappings": [
    {
      "guardFilePath": "rules/aws/secrets_manager/secretsmanager_scheduled_rotation_success_check.guard",
      "controls": [
        "AC-2(1)",
        "AC-2(j)"
      ]
    },
    {
      "guardFilePath": "rules/aws/iam/iam_user_group_membership_check.guard",
      "controls": [
        "AC-2(1)",
        "AC-2(j)",
        "AC-3",
        "AC-6"
      ]
    }
  ]
}
```