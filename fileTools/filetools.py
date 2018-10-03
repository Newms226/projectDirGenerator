from pathlib import Path

import datetime, subprocess

def makeProjDir(rootDir: str, projectName: str, remotePath: str):
    init_git_repo(rootDir, projectName)

    projDirStr = rootDir + "/" + projectName
    Path(projDirStr + '/' + 'docs').mkdir()
    Path(projDirStr + '/' + 'test').mkdir()
    Path(projDirStr + '/' + 'builds').mkdir()
    Path(projDirStr + '/' + projectName + '_src').mkdir()
    generateBasicTextFile(projDirStr, 'readme')
    generateBasicTextFile(projDirStr, 'license')
    generateBasicTextFile(projDirStr, 'contributors', 'Michael Newman')
    generateBasicTextFile(projDirStr, 'versions', 'txt',
                          'v0.1.0 Generated on ' + datetime.datetime.now() +
                          '\n')

def init_git_repo(rootdir: str, projectname: str, remotePath: str):
    subprocess.run('cd ' + rootdir)
    subprocess.run('git init ' + projectname)

def generateBasicTextFile(dirstr: str, name: str, extension: str, initaltext:
        str):
    file = open(dirstr + "/" + name.upper() + "." + extension, "w+")
    file.write('########\n' + name.upper() + '\n########\n\n' + initaltext)
    file.close()

def finish(rootDir: str, remotePath: str):
    subprocess.run('cd ' + str)
    subprocess.run('git add .')
    subprocess.run("git commit -m \'initial commit, autogen.\'")
    subprocess.run("git push --set-upstream ")