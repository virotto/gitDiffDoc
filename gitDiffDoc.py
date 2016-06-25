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
        self.alteration = ""

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
output = commands.getoutput('git diff ' + before_id + ' ' + after_id).split('\n')
diffInfos = []
tmp = None
for elem in output:
    if elem.startswith('diff'):
        if tmp != None:
            diffInfos.append(tmp)
        tmp = DiffInfo()
    elif elem.startswith('--- '):
        tmp.oldFile = '.' + elem[5:]
    elif elem.startswith('+++ '):
        tmp.newFile = '.' + elem[5:]
    elif elem.startswith('-'):
        tmp.alteration += elem + '&#10;'    
    elif elem.startswith('+'):
        tmp.alteration += elem + '&#10;'
diffInfos.append(tmp)

#make diff file (after and before)
#make after
for info in diffInfos:
    if info.newFile != ".dev/null":
        if not os.path.exists(os.path.dirname("./DiffFiles/after/" + info.newFile)):
            os.makedirs(os.path.dirname("./DiffFiles/after/" + info.newFile));
        commands.getoutput('git show ' + after_id + ':' + info.newFile[2:] + ' > ./DiffFiles/after/' + info.newFile)
#make before
for info in diffInfos:
    if info.oldFile != ".dev/null":
        if not os.path.exists(os.path.dirname("./DiffFiles/before/" + info.oldFile)):
            os.makedirs(os.path.dirname("./DiffFiles/before/" + info.oldFile));
        commands.getoutput('git show ' + before_id + ':' + info.newFile[2:] + ' > ./DiffFiles/before/' + info.oldFile)

