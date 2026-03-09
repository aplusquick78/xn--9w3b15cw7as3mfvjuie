import os

# 파주퀵서비스 - 파주 전지역 (읍/면/동/신도시) 데이터
paju_data = [
    {
        "dist": "운정신도시",
        "towns": ["출판단지", "운정동", "교하동", "야당동", "다율동", "와동동", "목동동", "동패동", "문발동", "신촌동", "연다산동", "오도동", "하지석동", "서패동"]
    },
    {
        "dist": "금촌권역",
        "towns": ["금촌동", "아동동", "검산동", "맥금동", "금릉동"]
    },
    {
        "dist": "북부권역",
        "towns": ["문산읍", "파주읍", "법원읍", "적성면", "파평면", "군내면", "진동면"]
    },
    {
        "dist": "남부권역",
        "towns": ["산업단지", "조리읍", "광탄면", "탄현면", "월롱면"]
    }
]

def generate_paju_pages():
    # 1. 파주 전체 통합 페이지 생성
    reg_folder = "파주퀵서비스"
    os.makedirs(reg_folder, exist_ok=True)
    # 5282quick.com 및 신속한 배송 키워드 반영
    header = "---\nlayout: board\ntown: 파주\ntown_full: 경기도 파주시 신속한 배송\n---"
    with open(f"{reg_folder}/index.html", 'w', encoding='utf-8') as f:
        f.write(header)
    print(f"✔️ 통합 페이지 생성: {reg_folder}")

    # 2. 각 권역 및 동네별 페이지 생성
    for group in paju_data:
        dist_name = group['dist']
        
        # 권역별 폴더 생성 (예: 운정신도시퀵서비스)
        dist_folder = f"{dist_name}퀵서비스"
        os.makedirs(dist_folder, exist_ok=True)
        with open(f"{dist_folder}/index.html", 'w', encoding='utf-8') as f:
            # 신속한 배송 키워드 강제 삽입
            f.write(f"---\nlayout: board\ntown: {dist_name}\ntown_full: 경기도 파주시 {dist_name} 신속한 배송\n---")
        print(f"✔️ 권역 페이지 생성: {dist_folder}")

        for town_name in group['towns']:
            # 동네 폴더 생성 (예: 문산읍퀵서비스)
            folder_name = f"{town_name}퀵서비스"
            os.makedirs(folder_name, exist_ok=True)
            
            # 레이아웃 board 유지 및 신속한 배송 정보 삽입
            content = f"---\nlayout: board\ntown: {town_name}\ntown_full: 경기도 파주시 {dist_name} {town_name} 신속한 배송\n---"
            
            with open(f"{folder_name}/index.html", 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✔️ 생성 완료: {folder_name}")

if __name__ == "__main__":
    generate_paju_pages()
    print("\n🚀 파주 전지역(읍/면/동/신도시) 타겟 페이지 생성이 완료되었습니다!")
    print("✅ 이제 깃허브에 올리시면 파주퀵서비스.8222quick.com에 즉시 반영됩니다.")
