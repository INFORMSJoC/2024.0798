import subprocess
import os

timeout_s = 5000

instance_dir = " " #path to the instances
log_file_KP= "KP.log"
log_file_AP= "AP.log"

#KP instances
for i in range(10,101,10):
    for j in range(1,11):
        instance = "KP_p-3_n-" + str(i) + "_ins-" + str(j)+".dat"
        try:
            subprocess.run(
                ["~/.local/bin/TanVan19-exe","KP", "twostage",1,instance_dir + instance,log_file_KP],timeout=timeout_s)
        except subprocess.TimeoutExpired:
            print("Timeout Algorithm TamVan for instance " + instance + " for ", timeout_s)


#AP instances
for i in range(5,51,5):
    for j in range(1,11):
        instance = "AP_p-3_n-" + str(i) + "_ins-" + str(j)+".dat"
        try:
            subprocess.run(
                ["~/.local/bin/TanVan19-exe", "AP", "twostage", 1, instance_dir + instance, log_file_AP],
                timeout=timeout_s)
        except subprocess.TimeoutExpired:
            print("Timeout Algorithm TamVan for instance " + instance + " for ", timeout_s)

