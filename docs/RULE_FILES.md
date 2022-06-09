# Developing Rule Files

The intent of AWS Guard Rules registry is to create modular single file guard rule files that can be mapped into multiple managed rule sets.

The `rules` directory has multiple sub-directories based on different technologies, providers and services.
    ```
    rules
    ├── aws
    │   └── apigateway
    │       │   ├── apigw_method_auth_type_is_not_none.guard
    │       │   └── tests
    │       │       └── apigw_method_auth_type_is_not_none_tests.yml
    │       └── dynamodb
    │           ├── dynamodb_pitr_enabled.guard
    │           └── tests
    │               └── dynamodb_pitr_is_enabled_tests.yml
    ├── kubernetes
    └── terraform
    ```
