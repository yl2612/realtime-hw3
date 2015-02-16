#!/usr/bin/env python
import sys
import re
page_count_dict = {}
page_final_dict = {}
for line in sys.stdin:
    line = line.strip()
    (word, count) = line.split("\t")
    #page_count_dict = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}
    count_list = count.strip("[]").split(",")
    rank = count_list[-1].strip()

    
    if word in page_count_dict:
        try:
            page_count_dict[word] += float(rank)
        except:
            page_final_dict[word] = count_list
    else:
        try:
            page_count_dict[word] = float(rank)
        except:
            page_final_dict[word] = count_list

#page_final_dict = dict(((key, [page_link_dict[key], page_count_dict[key]]) for key in page_link_dict))

for key in page_final_dict:
    page_final_dict[key].append(page_count_dict[key])
    print "%s\t%s" % (key,page_final_dict[key])

