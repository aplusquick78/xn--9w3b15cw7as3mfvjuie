import os

# 빠른배송 퀵서비스 성남 - 40개 지점 데이터
seongnam_data = [
    {
        "dist": "분당구",
        "towns": ["야탑동", "서현동", "이매동", "수내동", "정자동", "금곡동", "판교동", "삼평동", "백현동", "운중동", "구미동", "대장동", "석운동", "성남터미널", "분당", "야탑", "야탑터미널", "궁내동", "동원동", "율동", "분당동"]
    },
    {
        "dist": "수정구",
        "towns": ["복정동", "태평동", "수진동", "단대동", "산성동", "양지동", "창곡동", "신흥동"]
    },
    {
        "dist": "중원구",
        "towns": ["상대원동", "하대원동", "금광동", "은행동", "성남동", "여수동", "도촌동", "중동"]
    }
]

def generate_seongnam_pages():
    # 1. 성남시 전체 통합 페이지 생성
    reg_folder = "성남퀵서비스"
    os.makedirs(reg_folder, exist_ok=True)
    with open(f"{reg_folder}/index.html", 'w', encoding='utf-8') as f:
        # 빠른배송 컨셉 적용
        f.write(f"---\nlayout: board\ntown: 성남\ntown_full: 경기도 성남시 빠른배송\n---")
    print(f"✔️ 통합 페이지 생성: {reg_folder}")

    # 2. 각 구 및 동네별 페이지 생성
    for group in seongnam_data:
        dist_name = group['dist']
        
        # 구 페이지 생성 (예: 분당구퀵서비스)
        dist_folder = f"{dist_name}퀵서비스"
        os.makedirs(dist_folder, exist_ok=True)
        with open(f"{dist_folder}/index.html", 'w', encoding='utf-8') as f:
            f.write(f"---\nlayout: board\ntown: {dist_name}\ntown_full: 경기도 성남시 {dist_name} 빠른배송\n---")
        print(f"✔️ 구 페이지 생성: {dist_folder}")

        for town_name in group['towns']:
            # 동네 페이지 생성 (예: 야탑동퀵서비스)
            folder_name = f"{town_name}퀵서비스"
            os.makedirs(folder_name, exist_ok=True)
            
            # 레이아웃 board 유지 및 빠른배송 정보 삽입
            content = f"---\nlayout: board\ntown: {town_name}\ntown_full: 경기도 성남시 {dist_name} {town_name} 빠른배송\n---"
            
            with open(f"{folder_name}/index.html", 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✔️ 생성 완료: {folder_name}")

if __name__ == "__main__":
    generate_seongnam_pages()
    print("\n🚀 모든 지점(40개) 페이지 생성이 완료되었습니다!")

if __name__ == "__main__":
    generate_seongnam_pages()
    print("\n✅ 성남시 구/동별 모든 타겟 페이지 생성이 완료되었습니다.")
