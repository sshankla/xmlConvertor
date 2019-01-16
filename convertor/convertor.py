#/bash/python
# JDS Python Script for converting Geo CSV to XML
# Author: Suraj Shankla (suraj.shankla@jds.net.au) 
import xml.etree.ElementTree as ET
import os
import copy
'''sample.xml template for target xml
ld --> list of dictionary, each dictionary having
values to be populated'''

def readtemplate(xml):
    tree = ET.parse(xml)
    return tree

'''Create a copy of original list
and the sample.xml'''

def createlistofxmls(ld,sample_tree):
    target_list = []
  
    source_list = copy.copy(ld)
    ctr = 0

    for iter in source_list:
        sample_root = sample_tree.getroot()
        #print(iter)
        sample_root[0].attrib['from'] = iter['fromIP']
        sample_root[0].attrib['mask'] = iter['IPMask']
        # City would be Site Name (COL 5)
        sample_root[1].attrib['city'] = iter['SiteName']
        sample_root[1].attrib['country'] = iter['Country']
        sample_root[1].attrib['region'] = iter['Country'] + ', ' + iter['State']
        target_list.append(ET.tostring(sample_tree.getroot(),"UTF-8"))
        #print(target_list[ctr])
        ctr = ctr + 1


    return target_list



'''ld_values is list of dictionary
where each entry is a dictionary of values'''

def createlistofdict(ld_Values,csvfile):
        "List of all Lines"
        lines = csvfile.readlines()
        for iter in lines:
                temp_dict={}
                tokens=iter.split(',',9)
                #print(tokens)
                temp_dict['fromIP']=tokens[0]
                temp_dict['IPMask']=tokens[1]
                temp_dict['SubnetName']=tokens[2]
                temp_dict['SiteId']=tokens[3]
                temp_dict['SiteName']=tokens[4]
                temp_dict['Desc']=tokens[5]
                temp_dict['City']=tokens[6]
                temp_dict['State']=tokens[7]
                temp_dict['Country']=tokens[8]
                ld_Values.append(temp_dict)
        
        return ld_Values

'''lt --> list Of Tree Objects
spoolfile --> file where the xml would be written'''

def spoolvalues(ld,spoolfile):
        f = open(spoolfile,"a")
        for iter in ld:
                f.write(iter+'\n')
        
        return f

if __name__=='__main__':
    path=os.getcwd()
    sld=[]
    tree = readtemplate(path+'/sample.xml')
    csvfile=open(path+'/sample.data','r')
    sld=createlistofdict(sld,csvfile)
    tld=createlistofxmls(sld,tree)
    f=spoolvalues(tld,path+'/spool.data')
    f.close()



