import requests as rq
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn?order=reserve"
headers = {'User-Agent':'Chrome/76.0.3809.100'}
res = rq.get(url, headers = headers)

bs_obj = BeautifulSoup(res.content, 'lxml')

# print(bs_obj)

top = bs_obj.find('ul', class_='lst_detail_t1')
# liS = top.findAll('li', limit=1)
liS = top.findAll('li')


for li in liS:
    title = li.find('dt', class_='tit').find("a").text
    score = li.find('div', class_='star_t1').find('span', class_='num').text
    participants = li.find('div', class_='star_t1').find('span', class_='num2').text
    tmp_reserve = li.find('div', class_='star_t1 b_star')
    if tmp_reserve != None:
        reserve = tmp_reserve.find('span', class_='num').text
    else: reserve = ""
    tmp_li = li.find("dl", class_="info_txt1").find("dd").contents
    for item in tmp_li:
        if "개봉" in str(item):
            opendate = str(item).strip()
            break
    # print(len(tmp_li))
    # i = 1
    # for item in tmp_li:
    #    print(i, item)
    #    i += 1
    print("제목: ", title, " 평점: ", score, " 참여: ", participants, " 예약률: ", reserve, " 개봉일: ", opendate)



