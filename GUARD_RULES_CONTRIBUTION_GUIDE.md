# Guard Rules Contribution Guide

## Rules Directory Structure 

1. All Guard rules in this repository are stored under the `rules` directory.

2. The `rules` directory has multiple sub-directories based on different technologies, providers and services.
    ```
    rules
    ├── aws
    │   └── apigateway
    │       │   ├── apigw_method_auth_type_is_not_none.guard
    │       │   └── tests
    │       │       └── apigw_method_auth_type_is_not_none_tests.yml
    │       └── dynamodb
    │           ├── dynamodb_pitr_is_enabled.guard
    │           └── tests
    │               └── dynamodb_pitr_is_enabled_tests.yml
    ├── kubernetes
    └── terraform
    ```
## Rule Writing  

1. To understand the contribution process, let's consider an example of the `AWS DynamoDB Point-In-Time-Recovery` rule.

2. If the sub-directory for technology/provider/service doesn't already exist, create a new sub-directory under the appropriate path.
    ```
    mkdir rules/cloudformation/aws/dynamodb
    ```
3. Create a rule file with a `.guard` extension and the file name must match with the [AWS Config Managed rules](https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html) identifier in lower case.
    ```
    touch rules/cloudformation/aws/dynamodb/dynamodb_pitr_enabled.guard
    ```
4. Include the Config rule name and url at the top of the rule file.
    ```
    ## Config Rule Name : dynamodb-pitr-enabled
    ## Config Rule URL: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html"
    ```


4. Edit `dynamodb_pitr_enabled.guard` and describe bookkeeping for the rule, like rule intent and expectations.
    ```
    # Rule Intent: All DynamoDB Tables must have Point-In-Time-Recovery enabled

    # Expectations:
    # a) SKIP: when there are no DynamoDB Tables present
    # b) PASS: when all DynamoDB Tables have PITR enabled
    # c) FAIL: when all DynamoDB Tables have PITR disabled
    ```
5. Define variables required for a given rule and add comments to the rule wherever possible to make it easier for humans to understand.
    ```
    # Rule Intent: All DynamoDB Tables must have Point-In-Time-Recovery enabled

    # Expectations:
    # a) SKIP: when there are no DynamoDB Tables present
    # b) PASS: when all DynamoDB Tables have PITR enabled
    # c) FAIL: when all DynamoDB Tables have PITR disabled

    #
    # Select all DynamoDB Table resources from incoming template (payload)
    #
    let aws_dynamodb_table_resources = Resources.*[ Type == 'AWS::DynamoDB::Table' ]
    ```
6. Define a named rule block. The rule name should match with the rule file name. Named rule blocks allow for re-usability, improved composition and remove verbosity and repetition.
    ```
    # Rule Intent: All DynamoDB Tables must have Point-In-Time-Recovery enabled

    # Expectations:
    # a) SKIP: when there are no DynamoDB Tables present
    # b) PASS: when all DynamoDB Tables have PITR enabled
    # c) FAIL: when all DynamoDB Tables have PITR disabled

    #
    # Select all DynamoDB Table resources from incoming template (payload)
    #
    let aws_dynamodb_table_resources = Resources.*[ Type == 'AWS::DynamoDB::Table' ]


    rule dynamodb_pitr_enabled when %aws_dynamodb_table_resources !empty {

    }
    ```
7. Write rule clauses inside the named rule block. Please add a `custom message` to each clause. The `custom message` is expressed as `<<message>>` where 'message' is any string which ideally provides information regarding the clause preceding it. 
    ```
    ## Config Rule Name : dynamodb-pitr-enabled
    ## Config Rule URL: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html"

    # Rule Intent: All DynamoDB Tables must have Point-In-Time-Recovery enabled

    # Expectations:
    # a) SKIP: when there are no DynamoDB Tables present
    # b) PASS: when all DynamoDB Tables have PITR enabled
    # c) FAIL: when all DynamoDB Tables have PITR disabled

    #
    # Select all DynamoDB Table resources from incoming template (payload)
    #
    let aws_dynamodb_table_resources = Resources.*[ Type == 'AWS::DynamoDB::Table' ]


    rule dynamodb_pitr_enabled when %aws_dynamodb_table_resources !empty {
        # Ensure ALL DynamoDB Tables have Point-In-Time-Recovery enabled
        %aws_dynamodb_table_resources.Properties.PointInTimeRecoverySpecification.PointInTimeRecoveryEnabled == true 
            <<
            Point In Time Recovery must be enabled for strong resiliency
            >>
    }
    ```

## Writing unit tests
1. Now, let's write tests for the `dynamodb_pitr_is_enabled` rule. Before we write any code, create a `tests` directory under the appropriate path if it is not present.
    ```
    mkdir rules/cloudformation/aws/dynamodb/tests
    ```
2. Create a test file with `.yml` or `.json` extension and the file name must match with the `<rulename>_tests` format.
    ```
    touch rules/cloudformation/aws/dynamodb/tests/dynamodb_pitr_is_enabled.tests.yml
    ```
3. Edit `dynamodb_pitr_is_enabled.tests.yml` and start with writing tests for all `SKIP` expectations.
    ```
    ###
    # dynamodb-pitr-is-enabled test
    ###
    ---
    - name: Empty, SKIP
    input: {}
    expectations:
        rules:
        dynamodb_pitr_is_enabled: SKIP
    - name: No resources, SKIP
    input:
        Resources: {}
    expectations:
        rules:
        dynamodb_pitr_is_enabled: SKIP
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
        dynamodb_pitr_is_enabled: SKIP
    - name: No resources, SKIP
    input:
        Resources: {}
    expectations:
        rules:
        dynamodb_pitr_is_enabled: SKIP
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
        dynamodb_pitr_is_enabled: PASS
    ```
5. Finally, write tests for all `FAIL` expectations.
    ```
    ###
    # dynamodb-pitr-is-enabled test
    ###
    ---
    - name: Empty, SKIP
    input: {}
    expectations:
        rules:
        dynamodb_pitr_is_enabled: SKIP
    - name: No resources, SKIP
    input:
        Resources: {}
    expectations:
        rules:
        dynamodb_pitr_is_enabled: SKIP
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
        dynamodb_pitr_is_enabled: PASS
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
        dynamodb_pitr_is_enabled: FAIL
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
        dynamodb_pitr_is_enabled: FAIL
    ```
## Running unit tests
1. To run an individual unit test, execute the following command:
    ```
    bin/cfn-guard test --rules-file rules/cloudformation/aws/dynamodb/dynamodb_pitr_is_enabled.guard --test-data rules/cloudformation/aws/dynamodb/tests/dynamodb_pitr_is_enabled_tests.yml 
    ```
2. To run all tests in a directory, execute the following command:
    ```
    bin/cfn-guard test -d rules
    ```