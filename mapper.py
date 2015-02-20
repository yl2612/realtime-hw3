#!/usr/bin/env python
import re
import sys

for line in sys.stdin:          
    split_word = line.strip().split()
    li = split_word[0:-1]
    print '%s' % '\t'.join(map(str, li))
    for i in range(len(split_word)-2):
        mylist = [split_word[i+1], split_word[0], float(split_word[-1])/(len(split_word)-2)]      
        print '%s' % '\t'.join(map(str, mylist))