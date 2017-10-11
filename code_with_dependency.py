import numpy as np
import os

num_list = np.array([1,2,3,4,5])
avg = np.sum(num_list)/len(num_list)

fout = open("average.txt","w")
fout.write("Average is "+ str(avg))
fout.close()

print "Average is "+ str(avg)
print os.getenv("NAME","fromCode")

