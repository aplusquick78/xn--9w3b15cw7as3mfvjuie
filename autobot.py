import requests
from bs4 import BeautifulSoup
import datetime
import random
import os

# 파주시 타겟팅 (운정신도시, 금촌권역, 북부권역, 남부권역)
paju_areas = {
    "운정신도시": ["출판단지", "운정동", "교하동", "야당동", "다율동", "와동동", "목동동", "동패동", "문발동"],
    "금촌권역": ["금촌동", "아동동", "검산동", "맥금동", "금릉동"],
    "북부권역": ["문산읍", "파주읍", "법원읍", "적성면", "파평면"],
    "남부권역": ["산업단지", "조리읍", "광탄면", "탄현면", "월롱면"]
}

# 파주 전용 서비스 키워드
services = ["퀵서비스", "오토바이퀵", "다마스퀵", "라보퀵", "1톤용달"]

def get_random_keyword():
    # 파주 내에서 무작위 권역과 동 선택
    dist = random.choice(list(paju_areas.keys()))
    dong = random.choice(paju_areas[dist])
    
    town = f"파주 {dong}"
    town_full = f"파주시 {dist} {dong}"
    service = random.choice(services)
    return town, town_full, service

def get_naver_text(keyword):
    # 파주 관련 실시간 텍스트 크롤링
    url = f"https://search.naver.com/search.naver?where=view&query={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        descriptions = soup.select('.api_txt_lines.dsc_txt')
        text_list = [d.get_text() for d in descriptions[:5]]
        random.shuffle(text_list)
        return " ".join(text_list[:3])
    except:
        return f"{keyword} 전문 파주퀵서비스입니다. 신속한 배송을 약속드립니다."

def create_post():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    today_str = now.strftime("%Y-%m-%d")
    time_tag = now.strftime("%H%M%S")

    post_dir = '_posts'
    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
        
    town, town_full, service = get_random_keyword()
    # SEO를 위해 '파주'가 무조건 앞에 붙는 키워드 생성
    selected_keyword = f"{town_full} {service}"
    
    # 파일명 생성 (특수문자 제거)
    safe_keyword = selected_keyword.replace(' ', '-').replace('(', '').replace(')', '')
    file_path = f"{post_dir}/{today_str}-{time_tag}-{safe_keyword}.md"
    content_text = get_naver_text(selected_keyword)
    
    post_data = f"""---
layout: post
title: "{selected_keyword} 완료 리포트 - 파주퀵서비스"
date: {today_str}
town: "{town}"
town_full: "{town_full}"
---

### 🚀 {town} 현장 실시간 배송 소식

**파주퀵서비스**는 {town_full} 인근에서 가장 가까운 기사님을 매칭하는 스마트 시스템을 운영 중입니다. 고객님의 소중한 화물을 **신속한 배송** 원칙에 따라 안전하게 전달해 드렸습니다.

---

#### ✅ {service} 현장 리포트
{content_text}

---

#### ☎️ 파주 전지역 24시 접수
운정신도시, 문산, 금촌 등 파주 어디든 5~10분 이내 방문 픽업이 가능합니다.

* **대표번호: 1661-4262**
* **지원차종: 오토바이, 다마스, 라보, 1톤용달**
* **특화지역: 파주출판단지, LCD산업단지, 운정신도시 전문**

**신속한 배송** 파주퀵서비스였습니다.
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(post_data)
    print(f"🚀 [파주 특화모드] 파일 생성됨: {file_path}")

if __name__ == "__main__":
    create_post()
