#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,10,6,8,9,12,15]
use_sol_list=[0,1]

def NodeNamesSP1(seedvalue):
  file_name="results/CIFA_L3trace_use_0_binary_seed_"+str(seedvalue)+"_.txt"
  res_file="work/average/NodeNamesSP1_seed_"+str(seedvalue)+"_.txt"
  f1=open(res_file,'w')
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
	      	#if(int(fields[0])==1) and ((fields[1]=="bb-2") or (fields[1]=="bb-3") or (fields[1]=="bb-5") or (fields[1]=="router-gw-3")):
      		if((int(fields[0])==1) and (("producer" not in fields[1]) and ("malicious" not in fields[1]) and ("bb-" in fields[1]) and (fields[2]=="-1") and (fields[4]=="TimedOutInterests"))):
      			f1.write(fields[1])
      			f1.write("\t")
      			f1.write("---")
      			f1.write("\n")
      			
def NodeNamesSP2(seedvalue):
  file_name="results/CIFA_L3trace_use_0_binary_seed_"+str(seedvalue)+"_.txt"
  res_file="work/average/NodeNamesSP2_seed_"+str(seedvalue)+"_.txt"
  f1=open(res_file,'w')
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
	      	#if(int(fields[0])==1) and ((fields[1]=="bb-2") or (fields[1]=="bb-3") or (fields[1]=="bb-5") or (fields[1]=="router-gw-3")):
      		if((int(fields[0])==1) and (("good-leaf" in fields[1]) and (fields[2]=="-1") and (fields[4]=="TimedOutInterests"))):
      			f1.write(fields[1])
      			f1.write("\t")
      			f1.write("---")
      			f1.write("\n")
      			
def NodeNamesSP3(seedvalue):
  file_name="results/CIFA_L3trace_use_0_binary_seed_"+str(seedvalue)+"_.txt"
  res_file="work/average/NodeNamesSP3_seed_"+str(seedvalue)+"_.txt"
  f1=open(res_file,'w')
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
	      	#if(int(fields[0])==1) and ((fields[1]=="bb-2") or (fields[1]=="bb-3") or (fields[1]=="bb-5") or (fields[1]=="router-gw-3")):
      		if((int(fields[0])==1) and (("malicious" in fields[1]) and (fields[2]=="-1") and (fields[4]=="TimedOutInterests"))):
      			f1.write(fields[1])
      			f1.write("\t")
      			f1.write("---")
      			f1.write("\n")
def NodeNamesGenerate():
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		NodeNamesSP2(seedvalue)
		NodeNamesSP1(seedvalue)
		j=j+1
def main():
	NodeNamesGenerate()
if __name__=="__main__":
  main()
