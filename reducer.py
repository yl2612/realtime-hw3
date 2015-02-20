#!/usr/bin/env python
import sys
import re
page_count_dict = {}
page_final_dict = {}
for line in sys.stdin:
    split_word = line.strip().split()
    #page_count_dict = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}
    item = split_word[0]
    count_list = split_word[1:]
    rank = split_word[-1]
    
    if item in page_count_dict:
        try:
            page_count_dict[item] += float(rank)
        except:
            page_final_dict[item] = count_list
    else:
        try:
            page_count_dict[item] = float(rank)
        except:
            page_final_dict[item] = count_list

for key in page_final_dict:
    page_final_dict[key].append(page_count_dict[key])
    print key + "\t" + "%s" % "\t".join (map(str,page_final_dict[key]))