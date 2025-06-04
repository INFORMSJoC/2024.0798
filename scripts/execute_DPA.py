import subprocess
import os


timeout_s = 5000

dir= " " #path to dpa
instance_dir= " "  #path to the instances

#KP instances
for i in range(10,101,10):
    for j in range(1,11):
        instance = "KP_p-3_n-" + str(i) + "_ins-" + str(j)+".lp"
        try:
            subprocess.run(
                [dir + "DefiningPointAlgorithm-main/LinuxMake/main", instance_dir + instance], timeout=timeout_s)
        except subprocess.TimeoutExpired:
            print("Timeout Algorithm 1 for instanz " + instance + " for ", timeout_s)



#AP instances
for i in range(5,51,5):
    for j in range(1,11):
        instance = "AP_p-3_n-" + str(i) + "_ins-" + str(j)+".lp"
        try:
            subprocess.run(
                [dir + "DefiningPointAlgorithm-main/LinuxMake/main", instance_dir + instance], timeout=timeout_s)
        except subprocess.TimeoutExpired:
            print("Timeout Algorithm 1 for instanz " + instance + " for ", timeout_s)
