from functools import reduce, wraps

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


# wraps 를 사용하는 이유는 데코레이터를 썼을 떄 디버깅이 힘들기 떄문이다.
# 이는 함수가 한번 한번 감싸지기 때문에 함수의 고유의 정보가 감싸지는 함수에 숨겨져서 그렇다
# wraps 데코리이터를 사용하면 감싸지는 함수에도 원래 함수의 고유의 정보를 설정해주어 정보를 유지시켜준다.

"""
    # wrpas 소스 일부
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

"""

def without_wraps(func):
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper

def with_wraps(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper


@without_wraps
def my_func_a():
    """이것은 주석입니다"""
    a = "테스트 입니다 1"
    return a

@with_wraps
def my_func_b():
    """ 이것은 주석입니다 """
    a = "테스트 입니다 1"
    return a

print(my_func_a.__doc__)
print(my_func_a.__name__)

print(my_func_b.__doc__)
print(my_func_b.__name__)