#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,10,6,8,9,12,15]
use_sol_list=[0,1]
      			
def indiv_interest_metric(node_name,time,file_name,cible) :
  sum_interest=0.0
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
      		if((node_name == fields[1]) and (int(fields[0])==time)):
      			if( ("appFace://" in fields[3]) and (fields[4]==cible)):
      				sum_interest=sum_interest+float(fields[5])
  return sum_interest

def indiv_satisfaction_metric(node_name,time,file_name,cible) :
  sum_interest=0.0
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
      		if((node_name == fields[1]) and (int(fields[0])==time)):
      			if( ("appFace://" in fields[3]) and (fields[4]==cible)):
      				sum_interest=sum_interest+float(fields[5])
  return sum_interest

def AverageInterestAndSatisfaction_metric(seedvalue,use_sol):
  trace_file="results/CIFA_L3trace_use_"+str(use_sol)+"_rocket_seed_"+str(seedvalue)+"_.txt"
  res_file="work/average/AverageInterestRate_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
  f1=open(res_file,'w')
  res_file2="work/average/AverageSatisfactionRate_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
  f2=open(res_file2,'w')
  i=1
  node_names_file="work/average/NodeNamesSP2_seed_"+str(seedvalue)+"_.txt"
  while (i<=80):
  	sum_interest=0.0
  	sum_satisfRate=0.0
  	nb_node=0

  	with open(node_names_file,'r') as f:
  		for line in f:
  			fields=line.split("\t")
  			y_interest=indiv_interest_metric(fields[0],i,trace_file,"InInterests")
  			y_satisf=indiv_satisfaction_metric(fields[0],i,trace_file,"InSatisfiedInterests")
  			sum_interest=sum_interest+y_interest
  			if(float(y_interest)!=0.0):
	  			sum_satisfRate=sum_satisfRate+float(y_satisf)/float(y_interest)
  			nb_node=nb_node+1
  	average_interest_rate=float(sum_interest)/float(nb_node)
  	average_satisfaction_rate=float(sum_satisfRate)/float(nb_node)
  	f1.write(str(i))
  	f1.write("\t")
  	f1.write(str(average_interest_rate))
  	f1.write("\n")
  	  	
  	f2.write(str(i))
  	f2.write("\t")
  	f2.write(str(average_satisfaction_rate*100))
  	f2.write("\t")
  	f2.write(str(average_interest_rate))
  	f2.write("\t")
  	f2.write(str(sum_satisfRate))
  	f2.write("\t")
  	f2.write(str(nb_node))
  	f2.write("\n")
  	print("...............Interest and Satisfaction Rates For time.....",i,"UseSol:",use_sol,"SeedValue:",seedvalue)
  	i=i+1
  f1.close()
  
def AverageInterestAndSatisfactionGenerate():
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		i=0
		while(i<len(use_sol_list)):
			use_sol=use_sol_list[i]
			AverageInterestAndSatisfaction_metric(seedvalue,use_sol)
			i=i+1
		j=j+1
def AverageInterestRatePerTime(time,use_sol):
	sum_interest=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/average/AverageInterestRate_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_interest=sum_interest+float(fields[1])
					break
		j=j+1
	average_interest=float(sum_interest)/float(len(seed_list))
	return average_interest
	
def AverageSatisfactionRatePerTime(time,use_sol):
	sum_satisfaction=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/average/AverageSatisfactionRate_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_satisfaction=sum_satisfaction+float(fields[1])
					break
		j=j+1
	average_satisfaction=float(sum_satisfaction)/float(len(seed_list))
	return average_satisfaction
def AverageInterestAndSatisfaction(use_sol):
	i=1
	res_file_name="curves/average/AverageInterestRate_use_"+str(use_sol)+"_Final.txt"
	f1=open(res_file_name,'w')
	res_file_name2="curves/average/AverageSatisfactionRate_use_"+str(use_sol)+"_Final.txt"
	f2=open(res_file_name2,'w')
	while(i<=80):
		satisfaction_rate=AverageSatisfactionRatePerTime(i,use_sol)
		f2.write(str(i))
		f2.write("\t")
		f2.write(str(satisfaction_rate))
		f2.write("\n")
		i=i+1 
def main():
   print("...............Starting Interest And Satisfaction Rates.....")
   AverageInterestAndSatisfactionGenerate()
   AverageInterestAndSatisfaction(0)
   AverageInterestAndSatisfaction(1)
   
   print(".......................Finishing Interest And Satisfaction Rates.....")



if __name__=="__main__":
  main()
