import statistics
list1 = 35.8,37.8,40.4,38.1,36.3,42.6,40.6,35.5,37.4,49.1,35
print("mean")
print(statistics.fmean(list1))
print("median")
print(statistics.median(list1))
print("standard deviation")
print(statistics.stdev(list1))
print("sum")
print(sum(list1))
print("average")
print(sum(list1)/len(list1))
print("relative frequency")
for i in range (len(list1)):
    print(list1[i]/sum(list1))
