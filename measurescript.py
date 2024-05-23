import subprocess
import time


solver = './dpll'
cnf = './flat125-70.cnf'
measurements = []

for _ in range(10): 
    subprocess.run([solver, cnf], stdout=subprocess.PIPE)

for _ in range(40):
    start = time.time()
    subprocess.run([solver, cnf], stdout=subprocess.PIPE)
    end = time.time()
    measurements.append(end - start)
print(measurements)

