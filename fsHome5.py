# 자체 all, any
def my_all(args):
    for v in args:
        if not v:
            return False

    return True


def my_any(args):
    for v in args:
        if v:
            return True

    return False


print(my_all([1, 2, 0]))
print(my_all([1, 2, 3]))
print(my_any([1, 2, 0]))
print(my_any([0, 0, 0]))



# isnumeric 구현
def isnumeric(v):
    try:
        float(v)
        return True
    except:
        return False


print(isnumeric("abc"))
print(isnumeric("123"))
print(isnumeric("123.5"))
print(isnumeric("123.ab"))



# 제곱근 한없이 가까움
def calc_s (a, b):
    # a 의 제곱이 b 와 한없이 가깝다면 제곱근
    if abs(b - a ** 2) <= 0.0000001:
        return a
    else:
        a = (a + (b / a)) / 2
        return calc_s(a, b)


print(calc_s(10, 3))
print(calc_s(10, 4))
print(calc_s(10, 7))


#이전값과 차이 없음
def calc_s2 (a, b, c=None):
    # 어떤 0보다 큰 a를 선정한 뒤, a의 제곱이 b와 전에 값과 변함이 없다면..
    d = abs(b - a ** 2)

    if c is not None and c == d:
        return a
    else:
        a = (a + (b / a)) / 2
        return calc_s2(a, b, d)

print(calc_s2(10, 3))
print(calc_s2(10, 4))
print(calc_s2(10, 7))