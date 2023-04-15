#! /usr/bin/env python3
import os
import sys
seed_list=[1,5,2,14,10,6,8,9,12,15]
use_sol_list=[0,1]

def metric_throughput(node_name, file_name,cible,res_file_name) :
  resFinalList=[]
  resFinalList.clear()
  res_file="work/"+node_name+"_Throughput.txt"
  f1=open(res_file,'w')
  with open(file_name,'r') as f:
      for line in f:
      	fields=line.split("\t")
      	if(fields[0]!="Time"):
      	      	if((node_name in fields[1])): #and (int(fields[0])>=40)):
      	      		if( ("netdev://" in fields[3]) and (fields[4]==cible)):
      	      			f1.write(fields[0])
      	      			f1.write("\t")
      	      			f1.write(fields[6])
      	      			f1.write("\n")
  f1.close()
  last_time=1
  resFinalList.clear()
  sum_throughput=0.0
  with open(res_file,'r') as f:
  	for line in f:
  		fields=line.split("\t")
  		if(last_time==int(fields[0])):
  		        sum_throughput=sum_throughput+float(fields[1])
  		else:
  			resFinalList.append([last_time,sum_throughput*8])
  			last_time=int(fields[0])
  			sum_throughput=float(fields[1])
  	resFinalList.append([last_time,sum_throughput])
  f1=open(res_file_name,'w')
  for t in resFinalList:
   		f1.write(str(t[0]))
   		f1.write("\t")
   		f1.write(str(t[1]))
   		f1.write("\n")
  f1.close()
  			
def ThroughputGenerate(nd_name):
   	j=0
   	while(j<len(seed_list)):
   		seedvalue=seed_list[j]
   		i=0
   		while(i<len(use_sol_list)):
   			use_sol=use_sol_list[i]
   			file_name="results/CIFA_L3trace_use_"+str(use_sol)+"_binary_seed_"+str(seedvalue)+"_.txt"
   			result_file_name="work/"+nd_name+"_Throughput_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
   			metric_throughput(nd_name,file_name,"InData",result_file_name)
   			i=i+1
   		j=j+1

def AverageThroughputPerTime(nd_name,time,use_sol):
	sum_throughput=0.0
	j=0
	while(j<len(seed_list)):
		seedvalue=seed_list[j]
		file_name="work/"+nd_name+"_Throughput_use_"+str(use_sol)+"_seed_"+str(seedvalue)+"_.txt"
		with open(file_name,'r') as f:
			for line in f:
				fields=line.split("\t")
				if(int(fields[0])==time):
					sum_throughput=sum_throughput+float(fields[1])
					break
		j=j+1
	average_throughput_rate=float(sum_throughput)/float(len(seed_list))
	return average_throughput_rate
		
def AverageThroughput(nd_name,use_sol):
	i=1
	res_file_name="curves/"+nd_name+"_Throughput_use_"+str(use_sol)+"_Final.txt"
	f1=open(res_file_name,'w')
	while(i<=80):
		throughput_rate=AverageThroughputPerTime(nd_name,i,use_sol)
		f1.write(str(i))
		f1.write("\t")
		f1.write(str(throughput_rate))
		f1.write("\n")
		i=i+1
		
def FinalAverageThroughput():
	ThroughputGenerate("bb-2")
	AverageThroughput("bb-2",0)
	AverageThroughput("bb-2",1)
	ThroughputGenerate("bb-3")
	AverageThroughput("bb-3",0)
	AverageThroughput("bb-3",1)
	ThroughputGenerate("bb-5")
	AverageThroughput("bb-5",0)
	AverageThroughput("bb-5",1)
	ThroughputGenerate("gw-3")
	AverageThroughput("gw-3",0)
	AverageThroughput("gw-3",1)

def main():
   print("Starting Throughputs.....")
   FinalAverageThroughput()
   print("Finish Throughputs.....")



if __name__=="__main__":
  main()
