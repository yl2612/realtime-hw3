#!/usr/bin/env python
import re
import sys

for line in sys.stdin:          
    split_word = line.strip().split()
    print "%s\t%s" % (split_word[0], split_word[1:-1])
    for i in range(len(split_word)-2):
        print "%s\t%s" % (split_word[i+1], [split_word[0], float(split_word[-1])/(len(split_word)-2)])        
