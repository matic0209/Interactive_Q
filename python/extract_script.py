import re
from urllib import unquote
import ast
import email.utils
import numpy as np
import time
from collections import OrderedDict
from time import mktime
from datetime import datetime
def extract(fname, keyWord):
    fr = file(fname, "r")
    lines = fr.readlines()
    fr.close()
    sparqls = []
    i = 0
    
    lan_list = []
    var_list = []
    sys_list = []
    num_list = []
    for line in lines:
        map_tmp = { }
        str_or = line
        str_time = str_or.split('[',1)[1].split(']',1)[0];
        struct_time = time.strptime(str_time[:-6],"%d/%b/%Y %H:%M:%S")
        map_tmp['time']=datetime.fromtimestamp(mktime(struct_time))
        str_sparql = str_or.split('"',1)[1]
        str_sparql = str_sparql.split('"',1  )[0]
        map_tmp['str'] = unquote(str_sparql).replace("\n"," ")
        str_number = str_or.split('"',2)[2].strip()
        str_number = str_number.split(' ',3)
        ret_number = str_number[0]
        sys_number = str_number[1]
        map_tmp['num_ret'] = ret_number
        map_tmp['num_sys'] = sys_number
        str_var = str_number[2].strip('"').strip()
        str_lan = str_number[3].strip('"').strip()
        lan_list.append(str_lan)
        map_tmp['lan'] = str_lan
        map_tmp['var'] = str_var
        lan_list = list(OrderedDict.fromkeys(lan_list))
        #sparqls[i]=map_tmp
        sparqls.append(map_tmp)
    return sparqls    


if __name__ == "__main__":
    ret_map =  extract("../data/query_log/DBpedia_log_sample", "data")
    print len(ret_map)
    print ret_map[8]
