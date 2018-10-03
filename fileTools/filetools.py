import os
from pathlib import Path

import datetime


def makeProjDir(rootDir: str, projectName: str, remotePath: str):
    projDirStr = rootDir + "/" + projectName
    init_git_repo(rootDir, projDirStr)

    Path(projDirStr + '/' + 'docs').mkdir()
    Path(projDirStr + '/' + 'test').mkdir()
    Path(projDirStr + '/' + 'builds').mkdir()
    Path(projDirStr + '/' + 'env').mkdir()
    Path(projDirStr + '/' + 'resources').mkdir()
    Path(projDirStr + '/' + projectName + '_src').mkdir()
    generateBasicTextFile(projDirStr, 'readme', 'rst', "")
    generateBasicTextFile(projDirStr, 'license', 'rst', "")
    generateBasicTextFile(projDirStr, 'contributors', 'rst',
                          '  - Michael Newman')
    generateBasicTextFile(projDirStr, 'versions', 'rst',
                          'v0.1.0 Generated on '
                          + datetime.datetime.now().__str__() + '\n')

    initial_commit(projDirStr, remotePath)
    generate_branches(projDirStr)


def generateBasicTextFile(dirstr: str, name: str, extension: str, initaltext:
        str):
    file = open(dirstr + "/" + name.upper() + "." + extension, "w+")
    file.write(generate_reST_header(name) + initaltext)
    file.close()


def generate_reST_header(name: str):
    length = len(name)
    i = 0
    header = ""

    while i < length:
        header += "="
        i += 1

    return header + "\n" + name.capitalize() + "\n" + header + "\n"



def init_git_repo(rootDir: str, projectname: str):
    print('Attempting to create git repo at \"' + rootDir + "\" called \"" +
          projectname)
    os.system('cd ' + rootDir)
    os.system('git init ' + projectname)


def initial_commit(projdir: str, remotePath: str):
    os.system('cd ' + projdir)
    os.system('git add .')
    os.system('git status')
    os.system("git commit -m \'initial commit, autogen.\'")
    os.system("git remote add origin " + remotePath)
    os.system("git push -u origin master")


def generate_branches(rootdir: str):
    os.system('cd ' + rootdir)
    os.system('git checkout -b dev')
    os.system('git push --set-upstream origin dev')
