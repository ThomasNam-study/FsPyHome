import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(data)

print("각 요소에 3을 더하기")
print(data + 3)

print("각 요소에 3을 곱하기")
print(data * 3)

print("각 요소에 3 제곱")
print(data ** 3)

print("각 요소에 10 나누기")
print(data / 3)

# 타입 전환
print("float64 전환")
print(data.astype(np.float))

print("unicode 전환")
print(data.astype(np.unicode))

print("object 전환")
print(data.astype(np.object))

# ndArray 인덱스/슬라이스

# target : 6
print("target : 6")
print(data[1, 2])

# target : 5
print("target : 5")
print(data[1, 1])

# target : [[1, 2], [4,5]]
print("target : [[1, 2], [4,5]]")
print(data[0:2, 0:2])

# target : [[2, 3], [5,6], [8, 9]]
print("target : [[2, 3], [5,6], [8, 9]]")
print(data[:, 1:3])

# 1) 홀수인 숫자는 0으로 바꾸세요
print("1) 홀수인 숫자는 0으로 바꾸세요")
data[data % 2 == 1] = 0
print(data)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 2) 5보다 큰 숫자는 10으로 바꾸세요
print("2) 5보다 큰 숫자는 10으로 바꾸세요")
data[data > 5] = 10
print(data)

# 2) 5보다 큰 숫자는 10으로 바꾸세요

# 3) 제곱했을때 홀수인 숫자만 남기고 0으로 바꾸세요
print("3) 제곱했을때 홀수인 숫자만 남기고 0으로 바꾸세요")
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

data[data ** 2 % 2 == 0] = 0
print(data)