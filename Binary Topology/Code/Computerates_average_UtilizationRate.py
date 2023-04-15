#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,10,6,8,9,12,15]
#seed_list=[1]
use_sol_list=[0,1]
def indiv_utilization_metric(node_name,time,file_name) :
  sum_utiliz=0.0
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if((node_name == fields[1]) and (int(fields[0])==time)):
      		sum_utiliz=sum_utiliz+float(fields[3])
  return sum_utiliz

def AverageUtilization_metric(seedvalue,use_sol):
  trace_file="results/pitUtilization_use_"+str(use_sol)+"_binary_seed_"+str(seedvalue)+"_.txt"
  res_file="work/average/AverageUtilizationRate_use_"+str(use_sol)+"_binary_seed_"+str(seedvalue)+"_.txt"
  f1=open(res_file,'w')
  i=1
  node_names_file="work/average/NodeNamesSP1_seed_"+str(seedvalue)+"_.txt"
  while (i<=80):
  	sum_utiliz=0.0
  	nb_node=0
  	with open(node_names_file,'r') as f:
  		for line in f:
  			fields=line.split("\t")
  			y_utiliz=indiv_utilization_metric(fields[0],i,trace_file)
  			sum_utiliz=sum_utiliz+y_utiliz
  			nb_node=nb_node+1
  	average=float(sum_utiliz)/float(nb_node)
  	f1.write(str(i))
  	f1.write("\t")
  	f1.write(str(average))
  	f1.write("\n")
  	i=i+1
  f1.close()
  
def UtilizationRateGenerate():
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		i=0
		while(i<len(use_sol_list)):
			use_sol=use_sol_list[i]
			AverageUtilization_metric(seedvalue,use_sol)
			i=i+1
		j=j+1

def AverageUtilizationRatePerTime(time,use_sol):
	sum_utilization_rate=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/average/AverageUtilizationRate_use_"+str(use_sol)+"_binary_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_utilization_rate=sum_utilization_rate+float(fields[1])
					break
		j=j+1
	average_utilization_rate=float(sum_utilization_rate)/float(len(seed_list))
	return average_utilization_rate

def AverageUtilizationRate(use_sol):
	i=1
	res_file_name="curves/average/AverageUtilizationRate_use_"+str(use_sol)+"_Final.txt"
	f1=open(res_file_name,'w')
	while(i<=80):
		interest_rate=AverageUtilizationRatePerTime(i,use_sol)
		f1.write(str(i))
		f1.write("\t")
		f1.write(str(interest_rate))
		f1.write("\n")
		i=i+1
def main():
   print("Starting Rates.....")
   print("...............Starting Utilization.....")
   UtilizationRateGenerate()
   AverageUtilizationRate(0)
   AverageUtilizationRate(1)
   print(".......................Finishing Utilization.....")



if __name__=="__main__":
  main()
