# 튜플
# 불변 객체, 데이터를 추가할수 없고 수정할 수 없다.

# 리스트
# 수정 가능 객체, 데이터를 추가하거나 삭제 가능하다



# 본인 정보 dict 로 만들기
info = {}
info["name"] = "남한희"
info["age"] = 37
info["phone"] = "01053496254"
info["addr"] = "경기도 부천시"
info["sex"] = "남"

#print(info)

# 가족 정보 포함하여 리스트로 만들기
info2 = {}
info2["name"] = "정미진"
info2["age"] = 36
info2["phone"] = "01053496254"
info2["addr"] = "경기도 부천시"
info2["sex"] = "여"

#print(info)
#print(info2)

family = []
family.append(info)
family.append(info2)

#print(family)

# CSV 형태로 출력

keyLen = 0

for key in family[0]:

    if keyLen == len(family[0]) - 1:
        print(key)
    else:
        print(key, end=",")
        keyLen += 1

for o in family:
    i = 0
    for val in o.values():
        if i == keyLen:
            print(val)
        else:
            print(val, end=",")
            i += 1


# PEP20 에서 알파벳 갯수 출력

pep20 = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

adict = {}

for v in pep20:
    if not v.isalpha():
        continue

    v = v.lower()
    if v not in adict:
        adict[v] = 0

    adict[v] = adict[v] + 1

print(adict)


# 리스트 출력
list1 = [i for i in range(1, 6 + 1)]
list2 = [i for i in range(1, 6 + 1)[::-1]]
list3 = [[j for j in range(1, 3 + 1)] for i in range(1, 3 + 1)]
list4 = [[j for j in range(1 + (i * 3), 1 + (i * 3) + 3)] for i in range(0, 3)]
print(list1)
print(list2)
print(list3)
print(list4)