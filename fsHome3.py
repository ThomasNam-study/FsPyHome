import re
import string

# 참 10개, 거짓 10개

# True 를 의미
bool(True)
bool(1)
bool([1])
bool("a")
bool(1 == 1)
bool(1 > 0)
bool(1 < 2)
bool(1 & 1)
bool(1 | 0)
bool(1 and 1)

# False 를 의미
bool(False)
bool(0)
bool([])
bool("")
bool(1 != 1)
bool(1 > 1)
bool(1 < 1)
bool(1 & 0)
bool(0 | 0)
bool(1 and 0)

# all, any 추론
all([1, 0]) # False : 리스트의 모든 값이 참이여야 참
any([1, 0]) # True : 리스트의 하나의 값이 참이여도 참

all([])     # True : all 의 경우 리스트가 비어있다면 참이 된다 (의외임)
any([])     # False: any 의 경우 리스트가 ㄷ비어있다면 거짓이 된다 (이것도 의외임)

# 단어 역순 출력
v = input("단어를 입력하세요>> ")
print(v[::-1])

# palindrome 판별
q = ["Anna", "Radar", "Step on no Pets", "No lemon, no melon", "여보 안경 안보여.", "수박??? 박수!!!!"]

# 특수 문자 / 공백등을 찾는 정규식
onlyWordRe = re.compile("[" + string.punctuation + string.whitespace + "]")

for qs in q:
    qs2 = qs.lower()    # 모두 소문자로 변경
    qs2 = onlyWordRe.sub("", qs2)   # 특수 문자, 공백 정규식으로 모두 제거

    st = len(qs2) // 2

    f1 = qs2[0:st]
    f2 = qs2[-1:(st + 1) * -1:-1]

    if f1 == f2:
        print("%s is palindrome!" % (qs, ))
    else:
        print("%s is not palindrome!" % (qs,))

