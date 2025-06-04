import subprocess
import os

threads=[1,2,4,6,8,16]
#threads= [16,32,64,128] #threads for the second study
timeout_s = 5000

dir= " " #path to PEA
instance_dir= " "  #path to the instances
result_dir = " " #path to the results

#KP instances
for i in range(10,101,10):
    for j in range(1,11):
        for t in threads:
            instance = "KP_p-3_n-" + str(i) + "_ins-" + str(j)
            try:
                subprocess.run([dir+"PEA", instance_dir+instance+".lp",results_dir+instance+"_threads-"+str(t)+".json",str(t)],timeout=timeout_s)
            except subprocess.TimeoutExpired:
                print("Timeout Algorithm PEA for instance " + instance + " for ", timeout_s)
                

#AP instances
for i in range(5,51,5): #change to range(50,101,5) for the second study
    for j in range(1,11):
        for t in threads:
            instance = "AP_p-3_n-" + str(i) + "_ins-" + str(j)
            try:
                subprocess.run([dir+"PEA", instance_dir+instance+".lp",results_dir+instance+"_threads-"+str(t)+".json",str(t)],timeout=timeout_s)
            except subprocess.TimeoutExpired:
                print("Timeout Algorithm PEA for instance " + instance + " for ", timeout_s)
