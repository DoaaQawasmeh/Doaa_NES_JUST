#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,6,8,9,12,15]
use_sol_list=[0,1]

def indiv_throughput_metric(node_name,time,file_name,cible) :
  sum_throu=0.0
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
      		if((node_name == fields[1]) and (int(fields[0])==time)):
      			if( ("netdev://" in fields[3]) and (fields[4]==cible)):
      				sum_throu=sum_throu+float(fields[6])
  return sum_throu

def AverageThroughput_metric(seedvalue,use_sol):
  trace_file="results/CIFA_L3trace_use_"+str(use_sol)+"_rocket_seed_"+str(seedvalue)+"_.txt"
  res_file="work/average/AverageThroughput_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
  f1=open(res_file,'w')
  i=1
  node_names_file="work/average/NodeNamesSP1_seed_"+str(seedvalue)+"_.txt"
  while (i<=80):
  	sum_through=0.0
  	nb_node=0
  	with open(node_names_file,'r') as f:
  		for line in f:
  			fields=line.split("\t")
  			y_through=indiv_throughput_metric(fields[0],i,trace_file,"InData")
  			sum_through=sum_through+y_through
  			nb_node=nb_node+1
  	average=float(sum_through)/float(nb_node)
  	average=average*8
  	f1.write(str(i))
  	f1.write("\t")
  	f1.write(str(average))
  	f1.write("\n")
  	print("...............Throughput For time.....",i,"UseSol:",use_sol,"SeedValue:",seedvalue)
  	i=i+1
  f1.close()
  
def ThroughputGenerate():
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		i=0
		while(i<len(use_sol_list)):
			use_sol=use_sol_list[i]
			AverageThroughput_metric(seedvalue,use_sol)
			i=i+1
		j=j+1

def AverageThroughputPerTime(time,use_sol):
	sum_throughput=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/average/AverageThroughput_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_throughput=sum_throughput+float(fields[1])
					break
		j=j+1
	average_throughput=float(sum_throughput)/float(len(seed_list))
	return average_throughput

def AverageThroughput(use_sol):
	i=1
	res_file_name="curves/average/AverageThroughput_use_"+str(use_sol)+"_Final.txt"
	f1=open(res_file_name,'w')
	while(i<=80):
		through_rate=AverageThroughputPerTime(i,use_sol)
		f1.write(str(i))
		f1.write("\t")
		f1.write(str(through_rate))
		f1.write("\n")
		i=i+1
def main():
   print("Starting Rates.....")
   print("...............Starting Throughput.....")
   ThroughputGenerate()
   AverageThroughput(0)
   AverageThroughput(1)
   print(".......................Finishing Throughput.....")





if __name__=="__main__":
  main()
