#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = "virotto"
__version__ = "1.0"

import os
import sys
import commands
import cgi
import shutil

class DiffInfo:
    def __init__(self):
        self.oldFile = ""
        self.newFile = ""

after_id = "HEAD"
before_id = "HEAD~"
if len(sys.argv) == 2:
    after_id = sys.argv[1]
    before_id = after_id + '~'
if len(sys.argv) == 3:
    after_id = sys.argv[2]
    before_id = sys.argv[1]

if not os.path.exists(".git"):
    print ".git is not found"
    exit()
if os.path.exists("./DiffFiles"):
    shutil.rmtree("./DiffFiles")
os.makedirs("./DiffFiles");
os.makedirs("./DiffFiles/after");
os.makedirs("./DiffFiles/before");

#get Infos(git diff parser)
os.chdir(os.path.abspath(os.getcwd()))
output = commands.getoutput('git diff ' + before_id + ' ' + after_id + ' --name-status').split('\n')
diffInfos = []
tmp = None
for elem in output:
    tmp = DiffInfo()
    if elem.startswith('M'):
        tmp.oldFile = './' + elem[2:]
        tmp.newFile = './' + elem[2:]
    if elem.startswith('A'):
        tmp.oldFile = './' + elem[2:]
    if elem.startswith('D'):
        tmp.newFile = './' + elem[2:]
    diffInfos.append(tmp)

#make diff file (after and before)
#make after
for info in diffInfos:
    if info.newFile != "":
        if not os.path.exists(os.path.dirname("./DiffFiles/after/" + info.newFile)):
            os.makedirs(os.path.dirname("./DiffFiles/after/" + info.newFile));
        commands.getoutput('git show ' + after_id + ':' + info.newFile[2:] + ' > ./DiffFiles/after/' + info.newFile)
#make before
for info in diffInfos:
    if info.oldFile != "":
        if not os.path.exists(os.path.dirname("./DiffFiles/before/" + info.oldFile)):
            os.makedirs(os.path.dirname("./DiffFiles/before/" + info.oldFile));
        commands.getoutput('git show ' + before_id + ':' + info.newFile[2:] + ' > ./DiffFiles/before/' + info.oldFile)

