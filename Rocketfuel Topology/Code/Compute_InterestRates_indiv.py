#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,10,6,8,9,12,15]
use_sol_list=[0,1]

def metric_rate(node_name, file_name,cible,res_file_name) :
  resFinalList=[]
  resFinalList.clear()
  res_file="work/"+node_name+"Interest.txt"
  f1=open(res_file,'w')
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
      	      	if((node_name in fields[1])): #and (int(fields[0])>=40)):
      	      		if( ("netdev://" in fields[3]) and (fields[4]==cible)):
      	      			f1.write(fields[0])
      	      			f1.write("\t")
      	      			f1.write(fields[5])
      	      			f1.write("\n")

  f1.close()
  last_time=1
  resFinalList.clear()
  sum_interest=0.0
  with open(res_file,'r') as f:
  	for line in f:
  		fields=line.split("\t")
  		if(last_time==int(fields[0])):
  		        sum_interest=sum_interest+float(fields[1])
  		else:
  			resFinalList.append([last_time,sum_interest])
  			last_time=int(fields[0])
  			sum_interest=float(fields[1])
  	resFinalList.append([last_time,sum_interest])
  f1=open(res_file_name,'w')
  for t in resFinalList:
   		f1.write(str(t[0]))
   		f1.write("\t")
   		f1.write(str(t[1]))
   		f1.write("\n")
  f1.close()
  			
def InterestRateGenerate(nd_name):
   	j=0
   	while(j<len(seed_list)):
   		seedvalue=seed_list[j]
   		i=0
   		while(i<len(use_sol_list)):
   			use_sol=use_sol_list[i]
   			file_name="results/CIFA_L3trace_use_"+str(use_sol)+"_rocket_seed_"+str(seedvalue)+"_.txt"
   			result_file_name="work/"+nd_name+"InterestRate_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
   			metric_rate(nd_name,file_name,"InInterests",result_file_name)
   			i=i+1
   		j=j+1

def AverageInterestRatePerTime(nd_name,time,use_sol):
	sum_interest_rate=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/"+nd_name+"InterestRate_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_interest_rate=sum_interest_rate+float(fields[1])
					break
		j=j+1
	average_interest_rate=float(sum_interest_rate)/float(len(seed_list))
	return average_interest_rate
		
def AverageInterestRate(nd_name,use_sol):
	i=1
	res_file_name="curves/"+nd_name+"_InterestRate_use_"+str(use_sol)+"_Final.txt"
	f1=open(res_file_name,'w')
	while(i<=80):
		interest_rate=AverageInterestRatePerTime(nd_name,i,use_sol)
		f1.write(str(i))
		f1.write("\t")
		f1.write(str(interest_rate))
		f1.write("\n")
		i=i+1
		
def FinalAverageInterestRate():
	InterestRateGenerate("bb-469")
	AverageInterestRate("bb-469",0)
	AverageInterestRate("bb-469",1)
	InterestRateGenerate("bb-483")
	AverageInterestRate("bb-483",0)
	AverageInterestRate("bb-483",1)
	InterestRateGenerate("bb-627")
	AverageInterestRate("bb-627",0)
	AverageInterestRate("bb-627",1)
	InterestRateGenerate("gw-423")
	AverageInterestRate("gw-423",0)
	AverageInterestRate("gw-423",1)

def main():
   print("Starting InterestRates.....")
   FinalAverageInterestRate()
   print("Finish InterestRates.....")



if __name__=="__main__":
  main()
