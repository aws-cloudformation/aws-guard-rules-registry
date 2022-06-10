# AWS Guard Rules Registry

AWS Guard Rules Registry is an open-source repository of AWS `cfn-guard` rule files and managed rule sets. The intent of the registry is to give users AWS guard rules that provide policy as code solutions which compliment the AWS Config Managed Rules as well as custom developed Guard rules.

The Guard Rules Registry offers the following value:

* Easy to consume Managed Rules Sets based on sample AWS Conformance Packs. [see Getting Started]()
* Individual Guard Rule files corresponding to many of the AWS Config Managed Rules
* Rule Set Build process to compile single rule set files for public consumption

## About

The AWS Guard Rules Registry provides guard rules and prebuilt managed rule sets for implementing in policy-as-code initiatives. Many of the guard rules supported by AWS are guard rule implementation of AWS Config Managed Rules.

> **Note:** Not all AWS Config Managed Rules are present in the AWS Guard Rules Registry. Some of the AWS Config Managed Rules are detective only in nature and are not able to be validated in infrastructure as code relevant to development practices.

Within the Guard Rules Registry you will find cfn-guard Registry Rule files and builds of Managed Rule Sets.

### Registry Rules Files

The intent of AWS Guard Rules registry is to create modular single file guard rule files that can be mapped into multiple managed rule sets. AWS Guard Rules Registry contains individual guard rule files associated to a single rule. The [rules directory](/rules) contains multiple sub-directories based on different technologies, providers and services.

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

Many of the guard rules are supported by AWS and correspond to associated AWS Config Managed Rules. These rules can be identified by the all uppercase naming convention which is identical to the AWS Config Managed Rule identifier.

> **Note:** Guard rule names that are in all uppercase are intentionally set this way. The names reflects the AWS Config Managed rule identifier the guard rule is satisfying.

### Managed Rule Sets

AWS Guard Rules registry contains prebuilt managed rule sets compiled from rule mapping files found in the [mappings](/mappings) directory. The following managed Rule Sets are available for use:

| Rule Set                         | Rules Set File Name | Source Mapping File |
| -------------------------------- | -------- | ---------- |
| ABS Cloud Computing Implementation Guide 2.0 - Material Workloads | ABS_CCIGv2_Material | [Link](/mappings/rule_set_ABS_CCIGv2_Material.json) |
| ABS Cloud Computing Implementation Guide 2.0 | ABS-CCIGv2-Standard | [Link](/mappings/rule_set_ABS_CCIGv2_Standard.json) |
| Australian Cyber Security Centre (ACSC) Essential Eight Maturity Model | acsc_essential_8 | [Link](/mappings/rule_set_acsc_essential_8.json) |
| Australian Cyber Security Centre (ACSC) Information Security Manual (ISM) 2020-06 | acsc_ism | [Link](/mappings/rule_set_acsc_ism.json) |
| Australian Prudential Regulation Authority (APRA) CPG 234 | apra_cpg_234 | [Link](/mappings/rule_set_apra_cpg_234.json) |
| Bank Negara Malaysia (BNM) Risk Management in Technology (RMiT) | bnm_rmit | [Link](/mappings/rule_set_bnm_rmit.json) |
| Center for Internet Security (CIS) Amazon Web Services Foundation v1.4 Level 1 | cis_aws_benchmark_level_1 | [Link](/mappings/rule_set_cis_aws_benchmark_level_1.json) |
| Center for Internet Security (CIS) Amazon Web Services Foundation v1.4 Level2 | cis_aws_benchmark_level_2 | [Link](/mappings/rule_set_cis_aws_benchmark_level_2.json) |
| Center for Internet Security (CIS) Critical Security Controls v8 IG1 | cis_critical_security_controls_v8_ig1 | [Link](/mappings/rule_set_cis_critical_security_controls_v8_ig1.json) |
| Center for Internet Security (CIS) Critical Security Controls v8 IG2 | cis_critical_security_controls_v8_ig2 | [Link](/mappings/rule_set_cis_critical_security_controls_v8_ig2.json) |
| Center for Internet Security (CIS) Critical Security Controls v8 IG3 | cis_critical_security_controls_v8_ig3 | [Link](/mappings/rule_set_cis_critical_security_controls_v8_ig3.json) |
| Center for Internet Security (CIS) Top 20 Critical Security Controls | cis_top_20 | [Link](/mappings/rule_set_cis_top_20.json) |
| Cybersecurity & Infrastructure Security Agency (CISA) Cyber Essentials (CE) | cisa_ce | [Link](/mappings/rule_set_cisa_ce.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 1 | cmmc_level_1 | [Link](/mappings/rule_set_cmmc_level_1.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 2 | cmmc_level_2 | [Link](/mappings/rule_set_cmmc_level_2.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 3 | cmmc_level_3 | [Link](/mappings/rule_set_cmmc_level_3.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 4 | cmmc_level_4 | [Link](/mappings/rule_set_cmmc_level_4.json) |
| Cybersecurity Maturity Model Certification (CMMC) Level 5 | cmmc_level_5 | [Link](/mappings/rule_set_cmmc_level_5.json) |
| European Union Agency for Cybersecurity (ENISA) Cybersecurity guide for SMEs  | enisa_cybersecurity_guide_for_smes | [Link](/mappings/rule_set_enisa_cybersecurity_guide_for_smes.json) |
| Spain Esquema Nacional de Seguridad (ENS) High framework controls | ens_high | [Link](/mappings/rule_set_ens_high.json) |
| Spain Esquema Nacional de Seguridad (ENS) Low framework controls | ens_low | [Link](/mappings/rule_set_ens_low.json) |
| Spain Esquema Nacional de Seguridad (ENS) Medium framework controls | ens_medium | [Link](/mappings/rule_set_ens_medium.json) |
| Title 21 of the Code of Federal Regulations (CFR) Part 11 | FDA_21CFR_Part_11 | [Link](/mappings/rule_set_FDA_21CFR_Part_11.json) |
| Federal Risk and Authorization Management Program (FedRAMP) Moderate | fedramp_moderate | [Link](/mappings/rule_set_fedramp_moderate.json) |
| Federal Risk and Authorization Management Program (FedRAMP) Low | fedramp_low  | [Link](/mappings/rule_set_fedramp_low.json) |
| Federal Financial Institutions Examination Council (FFIEC) Cyber Security Assessment Tool domains | ffiec | [Link](/mappings/rule_set_ffiec.json) |
| Health Insurance Portability and Accountability Act (HIPAA) | hipaa_security | [Link](/mappings/rule_set_hipaa_security.json) |
| Korea – Information Security Management System (ISMS) | k_isms | [Link](/mappings/rule_set_k_isms.json) |
| Monetary Authority of Singapore (MAS) Notice 655 – Cyber Hygiene | mas_notice_655 | [Link](/mappings/rule_set_mas_notice_655.json) |
| Monetary Authority of Singapore (MAS) Technology Risk Managment Guidelines (TRMG) January 2021 | mas_trmg | [Link](/mappings/rule_set_mas_trmg.json) |
| National Bank of Cambodia’s (NBC) Technology Risk Management (TRM) Guidelines framework | nbc_trmg | [Link](/mappings/rule_set_nbc_trmg.json) |
| UK National Cyber Security Centre (NCSC) Cyber Assessment Framework (CAF) controls | ncsc_cafv3 | [rule_set_ncsc_cafv3.json](/mappings/rule_set_ncsc_cafv3.json) |
| K National Cyber Security Centre (NCSC) Cloud Security Principles | ncsc | [rule_set_ncsc.json](/mappings/rule_set_ncsc.json) |
| North American Electric Reliability Corporation Critical Infrastructure Protection Standards (NERC CIP) for BES Cyber System Information (BCSI), CIP-004-7 & CIP-011-3  | nerc | [Link](/mappings/rule_set_nerc.json) |
| NIST 1800-25 | nist_1800_25 | [Link](/mappings/rule_set_nist_1800_25.json) |
| NIST 800-171 | nist_800_171 | [Link](/mappings/rule_set_nist_800_171.json) |
| NIST 800-172 | nist_800_172 | [Link](/mappings/rule_set_nist_800_172.json) |
| NIST 800-181 | nist_800_181 | [Link](/mappings/rule_set_nist_800_181.json) |
| NIST 800-53 Revision 4 | nist800_53rev4 | [Link](/mappings/rule_set_nist800_53rev4.json) |
| NIST 800-53 Revision 5| nist800_53rev5 | [Link](/mappings/rule_set_nist800_53rev5.json) |
| NIST Cyber Security Framework (CSF)  | nist_csf | [Link](/mappings/rule_set_nist_csf.json) |
| NIST Privacy Framework | nist_privacy_framework | [Link](/mappings/rule_set_nist_privacy_framework.json) |
| New Zealand Government Communications Security Bureau (GCSB) Information Security Manual (NZISM) | nzism | [Link](/mappings/rule_set_nzism.json) |
| Payment Card Industry Data Security Standard (PCI DSS) 3.2.1 | pci_dss_3_2_1 | [Link](/mappings/rule_set_pci_dss_3_2_1.json) |
| Reserve Bank of India (RBI) Cyber Security Framework for Urban Cooperative Banks (UCBs) | rbi_bcsf_ucb | [Link](/mappings/rule_set_rbi_bcsf_ucb.json) |
| Reserve Bank of India (RBI) Master Direction – Information Technology Framework | rbi_md_itf | [Link](/mappings/rule_set_rbi_md_itf.json) |
| New York State Department Of Financial Services (NYDFS) cybersecurity requirements for financial services companies (23 NYCRR 500) | us_nydfs | [Link](/mappings/rule_set_us_nydfs.json) |
| Amazon Web Services' Well-Architected Framework Reliability Pillar | wa-Reliability-Pillar | [Link](/mappings/rule_set_wa-Reliability-Pillar.json) |
| AWS Guard rule set for Amazon Web Services' Well-Architected Framework Security Pillar | wa-Security-Pillar | [Link](/mappings/rule_set_wa-Security-Pillar.json) |

## Developing Custom Rule Sets

CFN-GUARD allows for teams to create multiple rule files and categorize them as a `rule set` so that you can validate your JSON- or YAML-formatted data against multiple rule files at the same time. The AWS Guard Rules Registry provides a centralized repository of Guard rule files which can be mapped into a rule set during the build process. To develop a rule set mapping file and submit your own Registry Rule Set see [CONTRIBUTING](CONTRIBUTING.md) for more information.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

