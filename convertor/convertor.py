#/bash/python
# JDS Python Script for converting Geo CSV to XML
# Author: Suraj Shankla (suraj.shankla@jds.net.au)
# Revised on 18th Jan, 2018. 
import xml.etree.ElementTree as ET
import os
import copy

'''sample.xml template for target xml
ld --> list of dictionary, each dictionary having
values to be populated'''

def readmappingconf(path):
        return open(path + '/convertor/mapping.conf','r')


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

'''Initiate accomplishes following:
    1. Finds the number of Keys for each element in ld_values
    2. Initiates a mapping of Keys and Columns based on mapping.conf'''

def initiate():
        mcf = readmappingconf(os.getcwd())

        value_column_mapping = {}
        number_of_mappings = 0
        for line in mcf:
                tokenlist = []
                tokenlist = line.split('=')
                if line[0] == 'V':
                        # Using -2 because -1 is carriage return '\n'
                        value_column_mapping[tokenlist[0]] = int(line[-2])-1 
                        number_of_mappings = number_of_mappings + 1
        
        config = (number_of_mappings,value_column_mapping)
        return config



'''Step 1: ld_values is list of dictionary
where each entry is a dictionary of values.
#############################################################
1. Change dated 18th Jan, 2018. 
Will Create a dictionary of values dynamically based number
of values specified in mapping.conf. 
ncreatelistofdict (list_of_dictionary,csvfile):list
#############################################################'''

def n_createlistofdict(ld_values,csvfile):

        return 1




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
    '''t = initiate()
    print(t[0],t[1])'''
    path=os.getcwd()
    sld=[]
    readmappingconf()
    tree = readtemplate(path+'/sample.xml')
    csvfile=open(path+'/sample.data','r')
    sld=createlistofdict(sld,csvfile)
    tld=createlistofxmls(sld,tree)
    f=spoolvalues(tld,path+'/spool.data')
    f.close()'''



