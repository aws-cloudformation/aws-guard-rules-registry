# Using Guard Rules Registry

The document details a *Getting Started* scenarios for AWS Guard Rules Registry. The Guard Rules Registry Rule Set mappings are built into supported release formats enabling quick and easy consumption. Since AWS Guard does not require access to your AWS environment, the static application security testing process can happen in a variety of CI platforms and services.

## Guard Rules Registry Rule Suppression

The rules build in the Guard Rules Registry support resource-level rule suppress. Suppressed Rules are marked as SKIP in the validation process. To suppress a rule add into the resource metadata the following `Metadata`:

**YAML:**
Suppressing rule `EC2_INSTANCE_PROFILE_ATTACHED`
```yaml
Resources:
  ExampleEC2:
    Type: AWS::EC2::Instance
    Metadata:
      guard:
        SuppressedRules:
        - EC2_INSTANCE_PROFILE_ATTACHED
```

**JSON:**
Suppressing rule `ELASTICSEARCH_ENCRYPTED_AT_REST`
```json
"Resources": {
  "ElasticsearchDomain": {
    "Type": "AWS::Elasticsearch::Domain",
    "Metadata": {
      "guard": {
        "SuppressedRules": ["ELASTICSEARCH_ENCRYPTED_AT_REST"]
      }
    },
    "Properties": {
      "DomainName": "test"
    }
  }
}
```

The intent of Guard rule suppression is to allow explicit and approved compliance exceptions to be documented and allowed at the code-base level. This facilitates a single compliance rule set to be used across an entire Organization while placing the rule deviations at the resource level. Changes are not made at the Guard Rules Registry rule set, but within the code-base. Auditing the code-base will show the rule exception intentionally/knowingly allowed while still allowing your CI testing to be successful.

## Guard Rules Registry Release Builds

Every merge into the main branch will produce a new `release` of all AWS Guard Rules Registry. View the latest release for download [here](https://github.com/aws-cloudformation/aws-guard-rules-registry/releases)

## Guard Rules Registry Local Development

To leverage the Guard Rules Registry Rule Sets, download the latest release or specific version you require in the releases and run via cfn-guard command line specifying the rule set file from the release via `--rules `:

```sh
cfn-guard validate --rules ./NIST800-53Rev4.guard --data myCloudFormation.yml --show-summary fail -p
```

## Guard Rules Registry Docker Builds

All AWS Guard Rule Registry are build into a Docker image with Guard installed. The release rule set files are built and copied into the Docker image allowing for simplified rule set specific. Follow these steps to pull the Docker image and view the available rule sets.

1. run: `docker pull public.ecr.aws/r7q6h7y6/guard:1.0.1`
2. enter the container to view available rules:
  ```
  docker run -it public.ecr.aws/r7q6h7y6/guard:1.0.1 sh
  ls
  ```
3. all rule sets are built into the root directory

> **Note:** The Docker image version identifies the release version. Using the `latest` tag will give you the latest release.

## AWS CodePipeline

*Coming Soon!*

## GitHub Actions

Leveraging the Docker image, a GitHub Action was created called [Guard Action](https://github.com/grolston/guard-action). Leverage or refactor this GitHub Action to fit your needs.

## Gitlab-CI

Gitlab-CI can leverage the AWS Guard Rules Registry docker image. The example below runs a

```yml
image:
  repository: public.ecr.aws/r7q6h7y6/guard
  tag: 1.0.1

stages:
 - ci

cfn-guard-job:
  stage: ci
  script:
    - cfn-guard validate --data ${INPUT_DATA_DIRECTORY} --rules /${INPUT_RULE_SET_NAME}.guard --show-summary fail -p

```
