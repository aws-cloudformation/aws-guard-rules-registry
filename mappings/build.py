#!/usr/bin/env python

import argparse
import os
import json
import glob
import re
import urllib.request

def download_resource_type_list():
  url = "https://cloudformation-schema.s3.us-west-2.amazonaws.com/resourcetypelist.json"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  return data

def create_guard_rules_registry_all_rules(dirName, version):
    aws_rules_directory =  dirName + '/rules/aws/**/*.guard'
    controls = ["all rules in AWS Guard Rules Registry"]
    mappings = []
    resource_list = download_resource_type_list()
    for build_file in glob.iglob(aws_rules_directory, recursive=True):
      reports_on = []
      build_file_relative_path = os.path.relpath(build_file)
      for resource in resource_list:
        with open(build_file) as build_file_contents:
          if re.search(resource, build_file_contents.read()) is not None:
            reports_on.append(resource)
      rule_json = {
        "guardFilePath": build_file_relative_path,
        "reportsOn": reports_on,
        "controls": controls
      }
      mappings.append(rule_json)
    all_rules_json = {
        "owner": "AWS",
        "ruleSetName": "guard-rules-registry-all-rules",
        "version": version,
        "description": "All AWS Guard Rules Registry in single rule set",
        "contact": "aws-guard-rules-registry@amazon.com",
        "mappings": mappings
    }
    with open('mappings/rule_set_guard_rules_registry_all_rules.json', 'w', encoding='utf-8') as outfile:
      json.dump(all_rules_json, outfile, ensure_ascii=False, indent=2)

def create_output_directory():
  path = "./docker/output/"
  isExist = os.path.exists(path)
  if not isExist:
    os.makedirs(path)


def check_build_skip(guard_file):
  skip = False
  # if file does not exist in mapping we will skip it
  file_exists = os.path.exists(guard_file)
  if file_exists:
    with open(guard_file) as f:
      firstline = f.readline().rstrip()
      if "## SKIP" in firstline:
        skip = True
    return skip
  else:
    skip = True
    print("file not found: " + guard_file )
  return skip

def build_custom_message(rule_set, control_list ):
  message = '''\
<<
    Guard Rule Set: {ruleset}
    Controls: {Control_List}\
    '''.format(ruleset=rule_set, Control_List=control_list )
  return message

def main(directory, version):
  create_guard_rules_registry_all_rules(directory, version)
  basedirectory =  directory + '/mappings/rule_set_*.json'
  create_output_directory()
  for build_file in glob.iglob(basedirectory, recursive=True):
    build_file_contents = open(build_file)
    data = json.load(build_file_contents)
    rule_set = data['ruleSetName']
    owner = data['owner']
    version = data['version']
    print(rule_set)
    for rule in data['mappings']:
      control_list = ",".join(rule['controls'])
      guard_file = rule["guardFilePath"]
      custom_message = build_custom_message(rule_set, control_list)
      if check_build_skip(guard_file) is False:
        inputfile = open(guard_file).read()
        output_file_name = "./docker/output/" + rule_set + ".guard"
        outputfile = open(output_file_name, "a")
        outputfile.write(re.sub('<<', custom_message, inputfile, flags=re.M))
        outputfile.write("\n")
        outputfile.close()
    # Closing file
    build_file_contents.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Guard Rules Registry Build')
  parser.add_argument("-d","--directory", required=False,default=os.getcwd(),help="Directory of the project rules")
  parser.add_argument("-r","--release", required=True,default="1.0.0",help="The release version for all rules file")
  args = parser.parse_args()
  directory = args.directory
  version = args.release
  main(directory, version)
