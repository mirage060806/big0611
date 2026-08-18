from urllib.request import urlopen
from bs4 import BeautifulSoup

# 주식 테이터 웹 크롤링과 테이터베이스 다루기
# 주식 사이트에 접속하기
# http://comp.fnguide.com

# 주식 데이터 크롤링
# 기본 정보 웹 크롤링

url = 'https://wcomp.fnguide.com/?c_id=AA&menu_type=01&cmp_cd=005930'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 날짜
date1 = soup.find('span', {'class':'date'})
print(date1.text)

# 날짜의 형식 변경
# [2026/08/14] -> 2026-08-14
date2 = date1.text
# replace(이전텍스트, 새텍스트)
date = date2.replace('[','').replace(']','').replace('/','-')
print(date)

# 종목 이름
corp_name1 = soup.find_all("h1", {"id":"giName"})
print(corp_name1)
# 출력: [<h1 id="giName">삼성전자</h1>]

# text 속성: 태그 내의 텍스트를 가져오기
corp_name = corp_name1[0].text
print(corp_name) # 출력: 삼성전자

# 종목 코드
code1 = soup.find_all("div", {"class":"corp_group1"})
code2 = code1[0].find("h2")
code = code2.text
print(code) # 출력: 005930

# 주가
stock_price1 = soup.find("tr", {"class":"rwf"})
# 1. r 클래스를 가진 td 태그를 먼저 찾습니다.
soup = stock_price1.find("td", {"class": "r"})

# 2. td 태그 바로 아래에 있는 첫 번째 텍스트 노드를 추출하고, 공백과 ',', '/'를 제거합니다.
stock_price1 = soup.find(string=True).replace('/', '').replace(',', '').strip()
stock_price = int(stock_price1)
print(stock_price)  # 출력: 279500

# 외국인 보유 비중
tr3 = soup.find_all("tr")[2]
fgn_own_ratio = float(tr3.find("td", {"class":"cle r"}).text)
print(fgn_own_ratio)

# 1Y 수익률
rel_return = float(tr3.find_all("span", {"class":"tcr"})[2].text)
print(rel_return)


# 상단 테이블 웹 크롤링
up_list = bs_obj.find("div", {"class":"corp_group2"})
# print(up_list)
ul = up_list.find_all("ul")
# print(ul)

# PER(Price Earning Ratio, 주가수익비율)
per = float(ul[0].find_all("li")[1].text)
print(per)

# 12M PER: 12개월 뒤의 예상 주가수익비율
per_12m = float(ul[1].find_all("li")[1].text)
print(per_12m)

# 업종 PER
per_ind = float(ul[2].find_all("li")[1].text)
print(per_ind)

# PBR(Price to Book Ratio, 주가순자산비율)
pbr = float(ul[3].find_all("li")[1].text)
print(pbr)

# 배당수익률
div_yid1 = ul[4].find_all("li")[1].text
div_yid2 = div_yid1.replace('%','')
div_yid = float(div_yid2)
print(div_yid)

# 시세현황 테이블 웹 크롤링
table1 = soup.find("div", {"id":"div1"})
table2 = table1.find_all("td")
print(table2)

# 거래량
volume1 = table2[1].text
volume = int(volume1.replace(',', '').strip())
print(volume)

# 거래대금
trans_price1 = table2[3].text
trans_price = int(trans_price1.replace(',', '').strip())
print(trans_price)

# 시가총액(우선주 포함)
mk_cpt_pfr1 = table2[6].text
mk_cpt_pfr = int(mk_cpt_pfr1.replace(',', '').strip())
print(mk_cpt_pfr)

# 시가총액(보통주)
mk_cpt_cm1 = table2[8].text
mk_cpt_cm = int(mk_cpt_cm1.replace(',', '').strip())
print(mk_cpt_cm)

# 결과 모음
res = [
    date, 
    corp_name, 
    code,
    stock_price,
    fgn_own_ratio,
    rel_return, 
    per, 
    per_12m, 
    per_ind, 
    pbr, 
    div_yid, 
    volume, 
    trans_price, 
    mk_cpt_pfr, 
    mk_cpt_cm
]

print(res)
print(len(res))