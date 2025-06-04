import subprocess
import os

timeout_s = 5000
threads= [1,2,4,6]
dir= " " #path to aira
instance_dir= " "  #path to the instances
result_dir = " " #path to the results

#KP instances
for i in range(10,101,10):
    for j in range(1,11):
        instance = "KP_p-3_n-" + str(i) + "_ins-" + str(j)+".lp"
        for t in threads:
            try:
                subprocess.run(
                    [dir + "moip_aira-main/build/src/aira","-p", instance_dir+instance,"-t", str(t),
                     "-o", result_dir+instance+"_threads-"+str(t)],timeout=timeout_s)
            except subprocess.TimeoutExpired:
                print("Timeout AIRA for instance " + instance + " for ", timeout_s)



#AP instances
for i in range(5,51,5):
    for j in range(1,11):
        instance = "AP_p-3_n-" + str(i) + "_ins-" + str(j)+".lp"
        for t in threads:
            try:
                subprocess.run(
                    [dir + "moip_aira-main/build/src/aira", "-p", instance_dir + instance, "-t", str(t),
                     "-o", result_dir  + instance + "_threads-" + str(t)], timeout=timeout_s)
            except subprocess.TimeoutExpired:
                print("Timeout AIRA  for instance " + instance + " for ", timeout_s)
