import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from operator import add
from time import time
import random

def time_simp(n):
    inside = 0
    time0 = time()  # start time
    for i in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 < 1:
            inside += 1
    return np.round(time() - time0, 3)  # timing operation

def time_spark(n):
    def circle_inside(p):
        x, y = random.random(), random.random()
        return 1 if x**2 + y**2 < 1 else 0
    
    time0 = time()  # start time
    sc.parallelize(range(0, n))  # creating spark dataset
      .map(circle_inside)
      .reduce(add)  # distribute calculation
    count = ...
    print("pi is %f" % (4.0 * count / n))
    print(np.round(time() - t_0, 3), " = time taken")
    return np.round(time() - time0, 3)  # timing operation

spark = SparkSession.builder.appName('Pi').getOrCreate()  # Creating spark session
sc = spark.sparkContext
P = []
N = [10000, 50000, 100000, 500000, 1000000, 5000000]
spk_exec_P = []
spk_P = []
for n in N:
    spk_P.append(time_spark(n))
    P.append(time_simp(n))
spark.stop()
spark = SparkSession.builder.appName('Pi').getOrCreate()  # Creating spark session
sc = spark.sparkContext
for n in N:
    spk_exec_P.append(time_spark(n))
spark.stop()

# plotting and labeling graph
plt.xlabel("Total points")  # Naming x-axis
plt.ylabel("pi estimation time")  # Naming y-axis
plt.xscale("log")
# labeling lines
plt.plot(N, spk_P, label="4 executions")  # threads
plt.plot(N, spk_exec_P, label="2 executions")
plt.plot(N, P, label="no parallelism")
plt.legend()  # give meaning to visualization
plt.show()  # display figure
