from functools import reduce

origin_list = list(range(1, 10+1))

print("origin : {}".format(origin_list))

#1. [3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

f1 = lambda x: x + 2
print("f1 : {}".format(list(map(f1, origin_list))))

#2. [1, 4, 9, 16, 25, 36, 49, 64 ,81, 100]

f2 = lambda x: x * x
print("f2 : {}".format(list(map(f2, origin_list))))

#3. [64, 81, 100]
print("f3 : {}".format(list(map(f2, filter(lambda x: x >= 8, origin_list)))))

#4. [55]
f4 = lambda x: sum(range(x + 1))
print("f4 : {}".format(list(map(f4, filter(lambda x:x >= 10, origin_list)))))

#5. 55
print("f5: {}".format(reduce(lambda x, y: x + y, origin_list)))

