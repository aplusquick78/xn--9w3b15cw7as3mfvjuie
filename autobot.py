import requests
from bs4 import BeautifulSoup
import datetime
import random
import os

# 성남시 타겟팅 (수정구, 중원구, 분당구 및 주요 동)
seongnam_areas = {
    "수정구": ["복정동", "태평동", "수진동", "단대동", "산성동", "양지동", "창곡동(위례)", "신흥동"],
    "중원구": ["상대원동", "하대원동", "금광동", "은행동", "성남동", "여수동", "도촌동"],
    "분당구": ["야탑동", "서현동", "이매동", "수내동", "정자동", "금곡동", "판교동", "삼평동", "백현동", "운중동", "구미동"]
}

# 성남 전용 서비스 키워드
services = ["퀵서비스", "오토바이퀵", "다마스퀵", "라보퀵", "1톤용달"]

def get_random_keyword():
    # 성남 내에서 무작위 구와 동 선택
    gu = random.choice(list(seongnam_areas.keys()))
    dong = random.choice(seongnam_areas[gu])
    
    town = f"성남 {dong}"
    town_full = f"성남시 {gu} {dong}"
    service = random.choice(services)
    return town, town_full, service

def get_naver_text(keyword):
    # 성남 관련 실시간 텍스트 크롤링
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
        return f"{keyword} 전문 성남퀵서비스입니다. 신속한 배송을 약속드립니다."

def create_post():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    today_str = now.strftime("%Y-%m-%d")
    time_tag = now.strftime("%H%M%S")

    post_dir = '_posts'
    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
        
    town, town_full, service = get_random_keyword()
    # SEO를 위해 '성남'이 무조건 앞에 붙는 키워드 생성
    selected_keyword = f"{town_full} {service}"
    
    file_path = f"{post_dir}/{today_str}-{time_tag}-{selected_keyword.replace(' ', '-')}.md"
    content_text = get_naver_text(selected_keyword)
    
    post_data = f"""---
layout: post
title: "{selected_keyword} 완료 리포트 - 성남퀵서비스"
date: {today_str}
town: "{town}"
town_full: "{town_full}"
---

### 🚀 {town} 현장 실시간 배송 소식

**성남퀵서비스**는 {town_full} 인근에서 가장 가까운 기사님을 매칭하는 스마트 오토포스팅 시스템을 운영 중입니다. 고객님의 소중한 화물을 **신속한 배송** 원칙에 따라 안전하게 전달해 드렸습니다.

---

#### ✅ {service} 현장 리포트
{content_text}

---

#### ☎️ 성남 전지역 24시 접수
성남시 수정구, 중원구, 분당구 어디든 5~10분 이내 방문 픽업이 가능합니다.

* **대표번호: 1661-4262**
* **지원차종: 오토바이, 다마스, 라보, 1톤용달**
* **특화지역: 판교테크노밸리, 야탑동, 상대원 공단 전문**

**신속한 배송** 성남퀵서비스였습니다.
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(post_data)
    print(f"🚀 [성남 특화모드] 파일 생성됨: {file_path}")

if __name__ == "__main__":
    create_post()
