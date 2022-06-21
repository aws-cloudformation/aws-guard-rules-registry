# Guard Rule Contribution Guide

The following details the development requirements to submit individual Guard rules for use in the Guard Rules Registry. The development conventions and standards allow Guard Rule Registry to be a modular and support Guard Rule Sets builds via the Guard Map process. All Guard Rule contributions must follow the standards in order for pull-request to be approved.

## Guidelines and Conventions Summary

This section provides general rules and conventions to follow when developing a Guard Rules Registry rule. For the detailed walk-though and reference go to [Rule Development Walk-through](#rule-development-walk-through).

**Guard Rule Files:**

* A single guard rule file will have a single rule block
* All Guard rule files should have a corresponding `[GUARD RULE FILE NAME]_tests.yml` file located in `tests` sub directory
* Guard Rule files are named in all lowercase and leverage snake case convention

**Guard Rules:**

* Guard `rule block` name should match with the rule file name. The only time it will differ is if the rule block is representing an AWS Config Managed Rule which will require the rule block name ot be all upper case while the file name be lower case
* Guard `rule blocks` will be in all lowercase unless it represents a corresponding AWS Config Managed Rule
* Guard rule file `Assignments` should be verbose and descriptive as possible to avoid naming conflicts during Rule Set mapping process (reference example [Rule Development Walk-through](#rule-development-walk-through) step 5)
* Guard Rules in the Rules Registry must support rule suppression at the resource level by defining a metadata exception.

**Guard Rule Custom Messages:**

* Guard rule block `custom messages` must have the starting `<<` and ending `>>` on their own lines. Do not shorten by placing the custom message in one line. This will break the Guard Mapping process for rule set builds (reference example [Rule Development Walk-through](#rule-development-walk-through) step 7)
* Guard rule block `custom messages` will document the `Violation;` and the recommended `Fix:` separated by a line break (reference example [Rule Development Walk-through](#rule-development-walk-through) step 8)

## Rules Directory Structure

1. All Guard rules in this repository are stored under the `rules` directory.
2. The `rules` directory has multiple sub-directories based on different technologies, providers and services.
    ```
    rules
    ├── aws
    │   └── apigateway
    │   │   ├── apigw_method_auth_type_is_not_none.guard
    │   │   └── tests
    │   │       └── apigw_method_auth_type_is_not_none_tests.yml
    │   └── dynamodb
    │       ├── dynamodb_pitr_enabled.guard
    │       └── tests
    │           └── dynamodb_pitr_is_enabled_tests.yml
    ├── kubernetes
    └── terraform
    ```
## Rule Development Walk-through

The following outlines the general process to develop individual AWS Guard Rules that work with the `Guard Rules Registry` and its `Guard Map Rule Sets`. Reference the complete individual [template file](../docs/_template/aws_managed_rule_identifier.guard) while developing new Guard Rules. Below outlines the details necessary of the referenced [template file](../rules/aws/_template/aws_managed_rule_identifier.guard).

1. To understand the contribution process, let's consider an example of the `AWS DynamoDB` `Point-In-Time-Recovery` rule.

2. If the sub-directory for technology/provider/service doesn't already exist, create a new sub-directory under the appropriate path.
    ```
    mkdir rules/cloudformation/aws/dynamodb
    ```
3. Create a rule file with a `.guard` extension using snake casing and all lower case. If the rule being developed is a best-effort Guard implementation, then file name must match with the [AWS Config Managed rules](https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html) identifier but still be in *lower case*.
    ```
    touch rules/aws/dynamodb/dynamodb_pitr_enabled.guard
    ```
4. Edit `dynamodb_pitr_enabled.guard` file and insert the [template header](../rules/aws/_template/aws_managed_rule_identifier.guard) filling out the necessary details. **Be sure to update the `Scenarios` section adding in any additional scenarios needed.** At minimum there should be in the order of SKIP, PASS, FAIL scenarios. The last required scenario defined should be a SKIP which represents a suppressed rule.
    ```
    #
    # Rule Identifier:
    #    DYNAMODB_PITR_ENABLED
    #
    # Description:
    #   Brief description of the rule
    #
    # Reports on:
    #    AWS::DynamoDB::Table
    #
    # Evaluates:
    #    AWS CloudFormation
    #
    # Rule Parameters:
    #    NA
    #
    # Scenarios:
    # a) SKIP: when there are no dynamodb table resource present
    # b) PASS: when all dynamodb table resources ObjectLockEnabled property is set to true
    # c) FAIL: when all dynamodb table resources do not have the ObjectLockEnabled property is set to true or is missing
    # d) SKIP: when metadata has rule suppression for DYNAMODB_PITR_ENABLED
    ```
5. Below the header, define the assignments required for a given rule and add comments to the rule wherever possible to make it easier for humans to understand. **AWS Guard Rules support rule suppression and requires you to add the guard rule name during variable assignment.** By adding in the `SuppressedRules` metadata, you override the rule within the code-base give ability to express rule exceptions at the code-level. **Assignment names should be try to unique within the Rules Registry. Be verbose and detailed in naming the assignment.**
    ```
    #
    # Select all DynamoDB Table resources from incoming template (payload)
    #
    let aws_dynamodb_table_resources_pitr = Resources.*[ Type == 'AWS::DynamoDB::Table'
      Metadata.guard.SuppressedRules not exists or
      Metadata.guard.SuppressedRules.* != "DYNAMODB_PITR_ENABLED" ## this is the name of the rule block
    ]
    ```
6. Define a named rule block. The rule name should match with the rule file name. **If the rule is to match an [AWS Config Managed Rule](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html), the rule name should match the AWS Config Identifier in upper case.** Named rule blocks allow for re-usability, improved composition and remove verbosity and repetition.
   ```
    rule DYNAMODB_PITR_ENABLED when %aws_dynamodb_table_resources_pitr !empty {

    }
    ```
7. Write rule clauses inside the named rule block. Please add a `custom message` to each clause. The `custom message` is expressed as `<<message>>` where 'message' is any string which ideally provides information regarding the clause preceding it. Please reference step 8 below for creating custom messages.
    ```
    ...

    rule DYNAMODB_PITR_ENABLED when %aws_dynamodb_table_resources_pitr_example !empty {
      # Ensure ALL DynamoDB Tables have Point-In-Time-Recovery enabled
      %aws_dynamodb_table_resources_pitr_example.Properties.PointInTimeRecoverySpecification.PointInTimeRecoveryEnabled == true
      <<
        Violation: All DynamoDB Tables must have Point-In-Time-Recovery enabled.
        Fix: Set the dynamodb table property PointInTimeRecoverySpecification.PointInTimeRecoveryEnabled to true.
      >>
    }
    ```
8. **Custom Message Blocks** - each rule block should contain single block multiline `custom message` containing `Violation:` and `Fix:` details. The `<<` and `>>` are to be set on their own lines without text. Example:
  ```
  <<
    Violation: All DynamoDB Tables must have Point-In-Time-Recovery enabled.
    Fix: Set the dynamodb table property PointInTimeRecoverySpecification.PointInTimeRecoveryEnabled to true.
  >>
  ```


## Writing Unit Tests
1. Now, let's write tests for the `DYNAMODB_PITR_ENABLED` rule. Before we write any code, create a `tests` directory under the appropriate path if it is not present.
    ```
    mkdir rules/cloudformation/aws/dynamodb/tests
    ```
2. Create a test file with `.yml` or `.json` extension and the file name must match with the `<rulename>_tests` format.
    ```
    touch rules/cloudformation/aws/dynamodb/tests/dynamodb_pitr_enabled.tests.yml
    ```
3. Edit `dynamodb_pitr_enabled_tests.yml` and start with writing tests for all `SKIP` expectations.
    ```
    ###
    # DYNAMODB_PITR_ENABLED tests
    ###
    ---
    - name: Empty, SKIP
    input: {}
    expectations:
        rules:
        DYNAMODB_PITR_ENABLED: SKIP
    - name: No resources, SKIP
    input:
        Resources: {}
    expectations:
        rules:
        DYNAMODB_PITR_ENABLED: SKIP
    ```
4. Next, write tests for all `PASS` expectations.
    ```
    ###
    # dynamodb-pitr-is-enabled test
    ###
    ---
    - name: Empty, SKIP
    input: {}
    expectations:
        rules:
        DYNAMODB_PITR_ENABLED: SKIP
    - name: No resources, SKIP
    input:
        Resources: {}
    expectations:
        rules:
        DYNAMODB_PITR_ENABLED: SKIP
    - name: DDB with PITR set to true, PASS
    input:
        Resources:
        Exampletable:
            Type: AWS::DynamoDB::Table
            Properties:
            KeySchema:
                - AttributeName: Id
                KeyType: HASH
            AttributeDefinitions:
                - AttributeName: Id
                AttributeType: S
                - AttributeName: dummy
                AttributeType: S
                - AttributeName: name
                AttributeType: S
                - AttributeName: owner
                AttributeType: S
                - AttributeName: createdAt
                AttributeType: S
            PointInTimeRecoverySpecification:
                PointInTimeRecoveryEnabled: true
    expectations:
        rules:
        DYNAMODB_PITR_ENABLED: PASS
    ```
5. Next, write tests for all `FAIL` expectations.
    ```
    - name: DDB with PITR set to false, FAIL
      input:
        Resources:
        Exampletable:
            Type: AWS::DynamoDB::Table
            Properties:
            KeySchema:
                - AttributeName: Id
                KeyType: HASH
            AttributeDefinitions:
                - AttributeName: Id
                AttributeType: S
                - AttributeName: dummy
                AttributeType: S
                - AttributeName: name
                AttributeType: S
                - AttributeName: owner
                AttributeType: S
                - AttributeName: createdAt
                AttributeType: S
            PointInTimeRecoverySpecification:
                PointInTimeRecoveryEnabled: false
      expectations:
        rules:
        DYNAMODB_PITR_ENABLED: FAIL

    - name: DDB with missing PITR property, FAIL
      input:
        Resources:
        Exampletable:
            Type: AWS::DynamoDB::Table
            Properties:
            KeySchema:
                - AttributeName: Id
                KeyType: HASH
            AttributeDefinitions:
                - AttributeName: Id
                AttributeType: S
                - AttributeName: dummy
                AttributeType: S
                - AttributeName: name
                AttributeType: S
                - AttributeName: owner
                AttributeType: S
                - AttributeName: createdAt
                AttributeType: S
      expectations:
        rules:
        DYNAMODB_PITR_ENABLED: FAIL
    ```
6. Finally, write tests for all `Suppressed` rules which will be have the `SKIP` expectations.
  ```
  - name: DDB with missing PITR property but rule suppression added, SKIP
      input:
        Resources:
        Exampletable:
            Type: AWS::DynamoDB::Table
            Metadata:
              guard:
                SuppressedRules:
                  - "DYNAMODB_PITR_ENABLED"
            Properties:
            KeySchema:
                - AttributeName: Id
                KeyType: HASH
            AttributeDefinitions:
                - AttributeName: Id
                AttributeType: S
                - AttributeName: dummy
                AttributeType: S
                - AttributeName: name
                AttributeType: S
                - AttributeName: owner
                AttributeType: S
                - AttributeName: createdAt
                AttributeType: S
      expectations:
        rules:
        DYNAMODB_PITR_ENABLED: SKIP
  ```

## Running unit tests and validations

All commands assume you are running from the the root of the project for current working directory.

1. To run an individual unit test, execute the following command:
    ```
    bin/cfn-guard test --rules-file rules/aws/dynamodb/dynamodb_pitr_enabled.guard --test-data rules/aws/dynamodb/tests/dynamodb_pitr_enabled_tests.yml
    ```
2. To run all tests in a directory, execute the following command:
    ```
    bin/cfn-guard test -d rules
    ```
3. To quickly discover and display the failed rules execute the following command:
    ```
    bin/cfn-guard test -d ./rules/ | grep "FAIL Rules:" -B 2 -A 1
    ```
4. To identify rules that have an error processing run the following command:
    ```
    bin/cfn-guard test -d ./rules/ | grep "Error processing" -B 2 -A 2
    ```