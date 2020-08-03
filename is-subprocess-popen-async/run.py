import subprocess
import time


n = 10

print("Begin program")

print("--- start: using run ---")
time_start = time.time()

def using_run():
    for i in range(10):
        proc = subprocess.run("sleep 0.2", capture_output=True, shell=True)
    
    # print("process:", proc)
    # print("stdout:", proc.stdout)
    # print("stderr:", proc.stderr)

using_run()

time_end = time.time()
print(f"`using_run` {n} times took {round(time_end - time_start, 3)} seconds to run.")
print("--- end: using run ---")

print("--- start: using Popen ---")
time_start = time.time()

l = []
for i in range(n):
    l.append(subprocess.Popen("sleep 0.2", shell=True))

[p.communicate() for p in l]

time_end = time.time()
print(f"`using_Popen` {n} times took {round(time_end - time_start, 3)} seconds to run.")
print("--- end: using Popen ---")

print("End program")
print("")
