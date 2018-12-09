import requests
import re
from bs4 import BeautifulSoup as bs

response = requests.get("http://www.0404.go.kr/dev/country.mofa?idx=&hash=&chkvalue=no2&stext=&group_idx=&alert_level=0")

bsObj = bs(response.text, "html.parser")

ul = bsObj.find("ul", {'class':'country_list'})

# 1) 가봉 2) 필리핀 3) 터키 4) 미국
crTargets = ["가봉", "필리핀", "터키", "미국"]
dist = {}


findCodeRe = re.compile("javascript:goview\\('(\d+)'\\);")

for li in ul.findAll("li"):

    # 크롤링 대상임
    if li.a.text in crTargets:
        f = findCodeRe.match(li.a["href"])

        if f:
            dist[crTargets.index(li.a.text)] = f.group(1)

            # 더이상 검색할 필요가 없다.
            if len(dist) == len(crTargets):
                break


print("원하는 국가를 선택하세요 ", end="")

for key in sorted(dist.keys()):
    print(" {}) {}".format(key + 1, crTargets[key]), end="")

print("")

key = input()

keyNum = int(key)

if keyNum < 1 or keyNum > len(crTargets):
    print("잘못된 값을 선택하셨습니다.")
else:
    v = "http://www.0404.go.kr/imgsrc.mofa?atch_file_id=COUNTRY_{}&file_sn=3".format(dist[keyNum - 1])
    print(v)
