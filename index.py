import configparser
import requests
import json
import subprocess
import os

CURRENT_PATH = os.getcwd()
config = configparser.ConfigParser()
config.read(os.path.join(CURRENT_PATH,
                         '/'.join(__file__.split('/')[:-1]), 'config.ini'))

if ('AUTH' not in config.sections()):
    config.add_section('AUTH')
if ('TOKEN' not in config['AUTH']):
    while True:
        AUTH_TOKEN = input('Please enter an authorization token: ')
        if (len(AUTH_TOKEN) > 39):
            break
        else:
            continue
    config['AUTH']['TOKEN'] = AUTH_TOKEN
    with open('config.ini', 'w') as configFile:
        config.write(configFile)

repositoryName = input('Repository name: ')
payload = {
    "name": repositoryName,
    "homepage": "https://github.com",
    "private": True,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True,
    "license_template": "mit",
    "auto_init": True
}

githubRequest = requests.post('https://api.github.com/user/repos',
                              data=json.dumps(payload),
                              headers={
                                  'Authorization': f"token {config['AUTH']['TOKEN']}",
                                  'Content-Type': "application/json",
                                  'Accept': "application/json"
                              }
                              )
sshUrl = json.loads(githubRequest.content.decode('utf8'))['ssh_url']

workingDir = os.path.join(CURRENT_PATH, repositoryName)
print(__file__)


""" WIP
subprocess.Popen(["mkdir", workingDir])
subprocess.Popen(["mkdir", repositoryName])
subprocess.Popen(["git", "-C", repositoryName, "init"])
subprocess.Popen(["git", "-C", repositoryName,
                  "remote", "add", "origin", sshUrl])
subprocess.Popen(
    ["git", "-C", repositoryName, "pull", "origin", "main"])
"""
