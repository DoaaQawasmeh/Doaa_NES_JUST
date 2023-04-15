#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,10,6,8,9,12,15]
use_sol_list=[0,1]

def utilization_metric(node_name,file_name,use_sol,res_file) :
  f1=open(res_file,'w')
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if((node_name in fields[1])): #and (int(fields[0])>=40)):
      		f1.write(fields[0])
	      	f1.write("\t")
	      	f1.write(fields[3])
  f1.close()
	
def UtilizationRateGenerate(nd_name):
   	j=0
   	while(j<len(seed_list)):
   		seedvalue=seed_list[j]
   		i=0
   		while(i<len(use_sol_list)):
   			use_sol=use_sol_list[i]
   			file_name="results/pitUtilization_use_"+str(use_sol)+"_rocket_seed_"+str(seedvalue)+"_.txt"
   			result_file_name="work/"+nd_name+"Utilization_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
   			utilization_metric(nd_name,file_name,use_sol,result_file_name)
   			i=i+1
   		j=j+1

def AverageUtilizationRatePerTime(nd_name,time,use_sol):
	sum_utilization_rate=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/"+nd_name+"Utilization_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_utilization_rate=sum_utilization_rate+float(fields[1])
					break
		j=j+1
	average_utilization_rate=float(sum_utilization_rate)/float(len(seed_list))
	return average_utilization_rate
		
def AverageUtilizationRate(nd_name,use_sol):
	i=1
	res_file_name="curves/"+nd_name+"_UtilizationRate_use_"+str(use_sol)+"_Final.txt"
	f1=open(res_file_name,'w')
	while(i<=80):
		interest_rate=AverageUtilizationRatePerTime(nd_name,i,use_sol)
		f1.write(str(i))
		f1.write("\t")
		f1.write(str(interest_rate))
		f1.write("\n")
		i=i+1
		
def FinalAverageUtilizationRate():
	UtilizationRateGenerate("bb-469")
	AverageUtilizationRate("bb-469",0)
	AverageUtilizationRate("bb-469",1)
	UtilizationRateGenerate("bb-483")
	AverageUtilizationRate("bb-483",0)
	AverageUtilizationRate("bb-483",1)
	UtilizationRateGenerate("bb-627")
	AverageUtilizationRate("bb-627",0)
	AverageUtilizationRate("bb-627",1)
	UtilizationRateGenerate("gw-423")
	AverageUtilizationRate("gw-423",0)
	AverageUtilizationRate("gw-423",1)

def main():
   print("Starting InterestRates.....")
   FinalAverageUtilizationRate()
   print("Finish InterestRates.....")



if __name__=="__main__":
  main()
