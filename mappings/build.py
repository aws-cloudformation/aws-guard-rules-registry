#!/usr/bin/env python

import argparse
import os
import json
import glob
import re

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

def main(directory):
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
        outputfile.close()
    # Closing file
    build_file_contents.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Guard Rules Registry Build')
  parser.add_argument("-d","--directory", required=False,default=os.getcwd(),help="Directory to download the audio to")
  args = parser.parse_args()
  directory = args.directory
  main(directory)
