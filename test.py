from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 브라우저 열기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.ticketlink.co.kr/sports/137/57")

# 페이지 로딩 대기
time.sleep(5)  # 콘텐츠가 JS로 로드되므로 충분히 기다려야 함

# 경기 카드 요소 찾기
game_items = driver.find_elements(By.CLASS_NAME, "match_schedule_item")

print(f"총 {len(game_items)}개의 경기가 검색되었습니다.\n")

# 각 경기에서 제목과 예매 버튼 정보 가져오기
for i, item in enumerate(game_items):
    try:
        title = item.find_element(By.CLASS_NAME, "match_title").text
        print(f"[{i+1}] 경기명: {title}")

        # 예매 버튼 클릭 (선택사항)
        reserve_button = item.find_element(By.TAG_NAME, "a")
        if reserve_button.text.strip() == "예매":
            print("  👉 예매 버튼 있음 → 클릭 시도")
            reserve_button.click()  # 실제 클릭하려면 주석 해제
        else:
            print("  ❌ 예매 버튼 없음")
    except Exception as e:
        print(f"[오류] 경기 정보 처리 중 문제가 발생했어요: {e}")

# 모든 작업 끝나면 브라우저 닫기 (선택)
# driver.quit()
