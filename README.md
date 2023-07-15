# AWS Guard Rules Registry

AWS Guard Rules Registry is an open-source repository of [AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) rule files and managed rule sets that help organizations *shift left* in their Software Development Life Cycle (SDLC) processes.

## TL;DR

**Leverage the existing AWS Guard Registry Rule Sets currently available:**
* Read the [Using Guard Rules Registry Guide](./docs/Using-Guard-Rules-Registry.md) for information on how to integrate into your existing continuous integration and development processes. Then pick from the list of [Guard Rules Registry Managed Rule Sets](#managed-rule-sets).

**Contribute to the individual AWS Guard Registry Rules:**
* Read the [Guard Rules Development Guide](./docs/Guard-Rules-Dev-Guide.md) for details in how to contribute and develop Guard Rules Registry rules. Additionally, Guard Rules Registry has several staged Guard rule files that have yet to be implemented. These Guard rules are to be a *best of effort* representation of AWS Config Managed rules. To get started look for an open issues labeled `good first issue`.

**Create and contribute your own open source AWS Guard Rules Registry custom rule set:**
* Read the [Guard Rule Sets Development Guide](./docs/Guard-Rule-Sets-Dev-Guide.md) for details on creating or updating the Guard Map rule set files.

## About

AWS Guard Rules Registry is an open-source repository of rule files and managed rule sets for AWS CloudFormation Guard. The intent of the registry is to give users Guard rules that provide policy as code solutions which complement the AWS Config Managed Rules as well as your Guard rules. Many of the Guard rules supported by AWS are best-effort Guard rule implementations of AWS Config Managed Rules.

> **Note:** Not all AWS Config Managed Rules are present in the AWS Guard Rules Registry. Some of the AWS Config Managed Rules are detective only in nature and are not able to be expressed in infrastructure as code relevant to development practices.

The Guard Rules Registry offers the following value:

* Easy to consume Managed Rules Sets based on many of the sample AWS Conformance Packs. *see [Guard Rules Registry Managed Rule Sets](#managed-rule-sets)*
* Individual Guard Rule files giving *best effort* to correspond to an AWS Config Managed Rule
* Rule Set mapping process to compile single rule set files for public consumption
* A centralized location for users, teams, and organizations to manage and open source their custom Guard rule sets
* Resource level rule suppress! See [Using Guard Rules Registry Rule Suppression](./docs/Using-Guard-Rules-Registry.md#guard-rules-registry-rule-suppression) for more details.

### Registry Rules Files

One of the intents of AWS Guard Rules Registry is to create modular single file Guard rule files that can be mapped into multiple managed rule sets similar to how AWS Config Conformance Packs work with AWS Config Managed Rules. The AWS Guard Rules Registry contains individual guard rule files associated to a single rule. The [rules directory](/rules) contains multiple sub-directories based on different technologies, providers, and services.

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

Many of the Guard rules are supported by AWS and correspond or complement associated AWS Config Managed Rules. These rules can be identified by the all-uppercase naming convention which is identical to the AWS Config Managed Rule identifier.

> **Note:** Guard rule names that are in all uppercase are intentionally set this way. The names reflects the AWS Config Managed rule identifier the guard rule is satisfying.

Within each directory that contains Guard rules, there is a `tests` sub-directory contains unit tests for some of the corner cases we expect Guard rule to `PASS`/`FAIL`/`SKIP`. The `test` sub-directory contains the corresponding test file for the Guard rule with the suffix `_tests` and can have the extension of `.yml` or `.json`. To learn more, see [Guard Rules Dev Guide](./docs/Guard-Rules-Dev-Guide.md#writing-unit-tests) for more detail on how to create unit tests for your guard rule.

### Managed Rule Sets

AWS Guard Rules registry contains prebuilt managed rule sets compiled from rule mapping files found in the [mappings](/mappings) directory. The following managed Rule Sets are available for use:

| Managed Rule Set                         | Rules Set Name | Mapping File |
| -------------------------------- | -------- | ---------- |
| ABS Cloud Computing Implementation Guide 2.0 - Material Workloads | ABS-CCIGv2-Material | [Link](/mappings/rule_set_ABS_CCIGv2_Material.json) |
| ABS Cloud Computing Implementation Guide 2.0 - Standard Workloads | ABS-CCIGv2-Standard | [Link](/mappings/rule_set_ABS_CCIGv2_Standard.json) |
| Australian Cyber Security Centre (ACSC) Essential Eight Maturity Model | acsc-essential-8 | [Link](/mappings/rule_set_acsc_essential_8.json) |
| Australian Cyber Security Centre (ACSC) Information Security Manual (ISM) 2020-06 | acsc-ism | [Link](/mappings/rule_set_acsc_ism.json) |
| Australian Prudential Regulation Authority (APRA) CPG 234 | apra-cpg-234 | [Link](/mappings/rule_set_apra_cpg_234.json) |
| Bank Negara Malaysia (BNM) Risk Management in Technology (RMiT) | bnm-rmit | [Link](/mappings/rule_set_bnm_rmit.json) |
| Center for Internet Security (CIS) Amazon Web Services Foundation v1.4 Level 1 | cis-aws-benchmark-level-1 | [Link](/mappings/rule_set_cis_aws_benchmark_level_1.json) |
| Center for Internet Security (CIS) Amazon Web Services Foundation v1.4 Level2 | cis-aws-benchmark-level-2 | [Link](/mappings/rule_set_cis_aws_benchmark_level_2.json) |
| Center for Internet Security (CIS) Critical Security Controls v8 IG1 | cis-critical-security-controls-v8-ig1 | [Link](/mappings/rule_set_cis_critical_security_controls_v8_ig1.json) |
| Center for Internet Security (CIS) Critical Security Controls v8 IG2 | cis-critical-security-controls-v8-ig2 | [Link](/mappings/rule_set_cis_critical_security_controls_v8_ig2.json) |
| Center for Internet Security (CIS) Critical Security Controls v8 IG3 | cis-critical-security-controls-v8-ig3 | [Link](/mappings/rule_set_cis_critical_security_controls_v8_ig3.json) |
| Center for Internet Security (CIS) Top 20 Critical Security Controls | cis-top-20 | [Link](/mappings/rule_set_cis_top_20.json) |
| Cybersecurity & Infrastructure Security Agency (CISA) Cyber Essentials (CE) | cisa-ce | [Link](/mappings/rule_set_cisa_ce.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 1 | cmmc-level-1 | [Link](/mappings/rule_set_cmmc_level_1.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 2 | cmmc-level-2 | [Link](/mappings/rule_set_cmmc_level_2.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 3 | cmmc-level-3 | [Link](/mappings/rule_set_cmmc_level_3.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 4 | cmmc-level-4 | [Link](/mappings/rule_set_cmmc_level_4.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 5 | cmmc-level-5 | [Link](/mappings/rule_set_cmmc_level_5.json) |
| European Union Agency for Cybersecurity (ENISA) Cybersecurity guide for SMEs  | enisa-cybersecurity-guide-for-smes | [Link](/mappings/rule_set_enisa_cybersecurity_guide_for_smes.json) |
| Spain Esquema Nacional de Seguridad (ENS) High framework controls | ens-high | [Link](/mappings/rule_set_ens_high.json) |
| Spain Esquema Nacional de Seguridad (ENS) Low framework controls | ens-low | [Link](/mappings/rule_set_ens_low.json) |
| Spain Esquema Nacional de Seguridad (ENS) Medium framework controls | ens-medium | [Link](/mappings/rule_set_ens_medium.json) |
| Title 21 of the Code of Federal Regulations (CFR) Part 11 | FDA-21CFR-Part-11 | [Link](/mappings/rule_set_FDA_21CFR_Part_11.json) |
| Federal Risk and Authorization Management Program (FedRAMP) Moderate | fedramp-moderate | [Link](/mappings/rule_set_fedramp_moderate.json) |
| Federal Risk and Authorization Management Program (FedRAMP) Low | fedramp-low  | [Link](/mappings/rule_set_fedramp_low.json) |
| Federal Financial Institutions Examination Council (FFIEC) Cyber Security Assessment Tool domains | ffiec | [Link](/mappings/rule_set_ffiec.json) |
| Health Insurance Portability and Accountability Act (HIPAA) | hipaa-security | [Link](/mappings/rule_set_hipaa_security.json) |
| Korea – Information Security Management System (ISMS) | k-isms | [Link](/mappings/rule_set_k_isms.json) |
| Monetary Authority of Singapore (MAS) Notice 655 – Cyber Hygiene | mas-notice-655 | [Link](/mappings/rule_set_mas_notice_655.json) |
| Monetary Authority of Singapore (MAS) Technology Risk Management Guidelines (TRMG) January 2021 | mas-trmg | [Link](/mappings/rule_set_mas_trmg.json) |
| National Bank of Cambodia’s (NBC) Technology Risk Management (TRM) Guidelines framework | nbc-trmg | [Link](/mappings/rule_set_nbc_trmg.json) |
| UK National Cyber Security Centre (NCSC) Cyber Assessment Framework (CAF) controls | ncsc-cafv3 | [Link](/mappings/rule_set_ncsc_cafv3.json) |
| UK National Cyber Security Centre (NCSC) Cloud Security Principles | ncsc | [Link](/mappings/rule_set_ncsc.json) |
| North American Electric Reliability Corporation Critical Infrastructure Protection Standards (NERC CIP) for BES Cyber System Information (BCSI), CIP-004-7 & CIP-011-3  | nerc | [Link](/mappings/rule_set_nerc.json) |
| NIST 1800-25 | nist-1800-25 | [Link](/mappings/rule_set_nist_1800_25.json) |
| NIST 800-171 | nist-800-171 | [Link](/mappings/rule_set_nist_800_171.json) |
| NIST 800-172 | nist-800-172 | [Link](/mappings/rule_set_nist_800_172.json) |
| NIST 800-181 | nist-800-181 | [Link](/mappings/rule_set_nist_800_181.json) |
| NIST 800-53 Revision 4 | nist800-53rev4 | [Link](/mappings/rule_set_nist800_53rev4.json) |
| NIST 800-53 Revision 5| nist800-53rev5 | [Link](/mappings/rule_set_nist800_53rev5.json) |
| NIST Cyber Security Framework (CSF)  | nist-csf | [Link](/mappings/rule_set_nist_csf.json) |
| NIST Privacy Framework | nist-privacy-framework | [Link](/mappings/rule_set_nist_privacy_framework.json) |
| New Zealand Government Communications Security Bureau (GCSB) Information Security Manual (NZISM) | nzism | [Link](/mappings/rule_set_nzism.json) |
| Payment Card Industry Data Security Standard (PCI DSS) 3.2.1 | PCI-DSS-3-2-1 | [Link](/mappings/rule_set_pci_dss_3_2_1.json) |
| Reserve Bank of India (RBI) Cyber Security Framework for Urban Cooperative Banks (UCBs) | rbi-bcsf-ucb | [Link](/mappings/rule_set_rbi_bcsf_ucb.json) |
| Reserve Bank of India (RBI) Master Direction – Information Technology Framework | rbi-md-itf | [Link](/mappings/rule_set_rbi_md_itf.json) |
| New York State Department Of Financial Services (NYDFS) cybersecurity requirements for financial services companies (23 NYCRR 500) | us-nydfs | [Link](/mappings/rule_set_us_nydfs.json) |
| Amazon Web Services' Well-Architected Framework Reliability Pillar | wa-Reliability-Pillar | [Link](/mappings/rule_set_wa-Reliability-Pillar.json) |
| AWS Guard rule set for Amazon Web Services' Well-Architected Framework Security Pillar | wa-Security-Pillar | [Link](/mappings/rule_set_wa-Security-Pillar.json) |


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

