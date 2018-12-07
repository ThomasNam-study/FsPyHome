from random import choice
from time import time

def check_time(func):
    def new_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()

        print("함수가 걸린 시간은 : ", end_time - start_time)
        return result
    return new_func

raw = list(range(-50, 50 + 1))

target = []

for _ in range(10):
    target.append(choice(raw))

# 삽입 정렬(揷入整列, insertion sort)은 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여,
# 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘이다.
# k번째 반복 후의 결과 배열은, 앞쪽 k + 1 항목이 정렬된 상태이다.
def insert_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        key = A[i]

        while A[j] > key and j >= 0:
            A[j + 1] = A[j]
            j = j - 1

        A[j + 1] = key

    return A

# 퀵정렬
def quick_sort(A):

    if len(A) <= 1:
        return A

    # 가운데를 피봇으로 선언한다.
    pivot = A[len(A) // 2]
    left_arr = []
    right_arr = []
    eq_arr = []

    for v in A:
        if v < pivot:
            left_arr.append(v)
        elif v > pivot:
            right_arr.append(v)
        else:
            eq_arr.append(v)

    return quick_sort(left_arr) + eq_arr + quick_sort(right_arr)

print(insert_sort(target))

target = []

for _ in range(10):
    target.append(choice(raw))

print(quick_sort(target))


# fibonacci 속도 향상
# 이부분은 진짜 모르겠어서 검색해봤습니다....
def fib2(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return (2 * fib2(n - 2)) + fib2(n - 3)


@check_time
def find_fib2(n):
    return fib2(n)

def fib(n):
    # F0 == 0
    # F1 = F2 = 1
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)

@check_time
def find_fib(n):
    return fib(n)

print(find_fib(32))
print(find_fib2(32))


# 어떤 0보다 큰 정수는, 짝수일때는 2로 나누고,
# 홀수일때는 3을 곱한 뒤 1을 더하는 작업을 반복한다고 했을때,
# 언젠가는 1이 됩니다.
# n을 받아서, 1부터 n까지 숫자를 위에 작업을 반복시켰을때,
# 몇번 연산하면 1이 되는지 리스트에 넣어 리턴하는 함수를 만드세요.
def num_func(v):
    if v % 2 == 0:
        # 짝수
        return v // 2
    else:
        # 홀수
        return (v * 3) + 1

def check_cnt(v):
    cnt = 1

    print("v : {}".format(v))

    if v == 1:
        return cnt

    while True:
        v = num_func(v)
        cnt += 1

        if v == 1:
            break

    return cnt

def calc_list(n):
    result = []
    for n1 in range(1, n + 1):
        result.append(check_cnt(n1))

    return result

print(calc_list(10))


# 어떤 0보다 큰 정수는, 짝수일때는 2로 나누고,
# 홀수일때는 3을 곱한 뒤 1을 더하는 작업을 반복한다고 했을때,
# 언젠가는 1이 됩니다.
# n을 받아서, 1부터 n까지 숫자를 위에 작업을 반복시켰을때,
# 몇번 연산하면 1이 되는지 리스트에 넣어 리턴하는 함수를 만드세요.
# Memorization

# num_func 은 그대로 이용

MEMO = {}

def check_cnt_mem(v):

    sv = v

    if MEMO.get(str(v)):
        return MEMO[str(v)]

    cnt = 1

    if v == 1:
        return cnt

    while True:
        v = num_func(v)
        cnt += 1

        if v == 1:
            MEMO[str(sv)] = cnt
            break
        elif MEMO.get(str(v)):
            # 이 다음에 횟수를 안다
            cv = cnt - 1 + MEMO[str(v)]
            MEMO[str(sv)] = cv
            return cv

    return cnt

def calc_list_mem(n):
    result = []
    for n1 in range(1, n + 1):
        result.append(check_cnt_mem(n1))

    return result

print(calc_list_mem(10))

# 위 문제를 다음과 같이 풀었을때,
# 현재 Memorization의 한계는 무엇인지 설명하고.
# Memorization을 더 향상시키기 위해 코드를 수정해보세요

# 문제점을 찾기가 너무 힘들었습니다. 다른분 풀이해주신거 보고 따라해봅니다....

MEMO = {}

def iter(a, n, cnt=1):
    if MEMO.get(n):
        cnt = MEMO[n] + ( cnt - 1 )
        MEMO.setdefault(a, cnt)
        return cnt

    if n == 1:
        MEMO.setdefault(a, cnt)
        return cnt

    cnt += 1

    if n % 2 == 0:
        return iter(a, n / 2, cnt)
    else:
        rcnt = iter(a, (n * 3) + 1, cnt)

        # 다른분꺼 보고 했는데.. 잘 이해가 안되네요...
        MEMO.setdefault((n * 3) + 1, rcnt - cnt + 1)

        return rcnt

def solution(n):
    result = []
    for i in range(1, n+1):
        result.append(iter(i, i))
    return result


print(solution(10))
