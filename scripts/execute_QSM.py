import subprocess
import os

threads=[1,2,4,6,8,16]
timeout_s = 5000

dir= " " #path to QSM
instance_dir= " "  #path to the instances
result_dir = " " #path to the results
#KP instances
for i in range(10,101,10):
    for j in range(1,11):
        for t in threads:
            instance = "KP_p-3_n-" + str(i) + "_ins-" + str(j)
            try:
                subprocess.run([dir+"QSM", instance_dir+".dat",str(t)],timeout=timeout_s)
                os.rename(dir+"Results.txt",results_dir+ instance+"_threads-"+ str(t)+".txt")
            except subprocess.TimeoutExpired:
                print("Timeout Algorithm QSM for instance " + instance + " and "+ str(t)+ " threads: ", timeout_s)


#AP instances
for i in range(50,51,5):
    for j in range(1,11):
        for t in threads:
            instance = "AP_p-3_n-" + str(i) + "_ins-" + str(j)
            try:
                subprocess.run([dir+"QSM", instance_dir+instance+".dat",str(t)],timeout=timeout_s)
                os.rename(dir+"Results.txt",results_dir+ instance+"_threads-"+ str(t)+".txt")
            except subprocess.TimeoutExpired:
                print("Timeout Algorithm QSM for instance " + instance + " and "+ str(t)+ " threads: ", timeout_s)

