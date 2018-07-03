#!/usr/bin/env python3
#coding:utf-8
import os
import sys
import re

test_h = open('test.vcf','w')

with open (sys.argv[1],'r') as f_h:
    for line in f_h:
        if re.search('^chry',line,re.IGNORECASE):
            infos = re.split('\t',line.strip())
            if infos[6] == "PASS":
                for info in re.split(';',infos[7]):
                    infos = re.split('=',info)
                    if infos[0] == 'DP' and int(infos[1]) > 100:
                        #print(line,end='');break;
                        test_h.write(line);break
f_h.close()
test_h.close()
