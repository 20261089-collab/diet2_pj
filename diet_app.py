import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="맞춤형 다이어트 도움 앱",
    page_icon="🥗",
    layout="centered"
)

# 2. 음식 데이터 정의
foods = {
    "김밥": {"calorie": 450, "type": "한식"},
    "참치김밥": {"calorie": 500, "type": "한식"},
    "치즈김밥": {"calorie": 530, "type": "한식"},

    "샐러드": {"calorie": 250, "type": "가벼운식단"},
    "닭가슴살": {"calorie": 165, "type": "단백질"},
    "고구마": {"calorie": 130, "type": "가벼운식단"},
    "현미밥": {"calorie": 320, "type": "한식"},

    "라면": {"calorie": 500, "type": "분식"},
    "불닭볶음면": {"calorie": 530, "type": "분식"},
    "짜장면": {"calorie": 700, "type": "중식"},
    "짬뽕": {"calorie": 650, "type": "중식"},

    "햄버거": {"calorie": 550, "type": "패스트푸드"},
    "치킨": {"calorie": 700, "type": "패스트푸드"},
    "피자": {"calorie": 800, "type": "패스트푸드"},

    "떡볶이": {"calorie": 450, "type": "분식"},
    "순대": {"calorie": 300, "type": "분식"},

    "계란": {"calorie": 80, "type": "단백질"},
    "바나나": {"calorie": 90, "type": "간식"},
    "사과": {"calorie": 100, "type": "간식"},
    "요거트": {"calorie": 120, "type": "간식"},

    "연어": {"calorie": 250, "type": "단백질"},
    "스테이크": {"calorie": 600, "type": "단백질"},

    "파스타": {"calorie": 650, "type": "양식"},
    "샌드위치": {"calorie": 400, "type": "간단식"},
    "초밥": {"calorie": 500, "type": "일식"}
}

# 3. 세션 상태 초기화 (버튼 클릭 상태 유지용)
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# 앱 제목
st.title("🥗 맞춤형 다이어트 도움 앱")
st.caption("사용자 정보 기반 식단 및 운동 추천 시스템")

st.divider()

# 4. 사용자 정보 입력 영역
st.header("👤 사용자 정보 입력")

name = st.text_input("이름")

gender = st.selectbox(
    "성별",
    ["여자", "남자"]
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("나이", min_value=1, step=1)

with col2:
    height = st.number_input("키(cm)", min_value=1.0)

with col3:
    weight = st.number_input("몸무게(kg)", min_value=1.0)

activity = st.selectbox(
    "활동량",
    ["거의 안 움직임", "보통", "운동 자주 함"]
)

goal = st.selectbox(
    "목표",
    ["감량", "유지", "근육증가"]
)

allergy = st.text_input(
    "알레르기 음식 (없으면 없음 입력)",
    value="없음"
)

dislike = st.text_input(
    "싫어하는 음식 (없으면 없음 입력)",
    value="없음"
)

food_style = st.selectbox(
    "선호 식단",
    ["한식", "가벼운식단", "단백질", "간단식", "분식", "중식", "양식", "일식", "간식", "패스트푸드"]
)

st.divider()

# 5. 분석 시작 버튼
if st.button("✨ 사용자 분석 시작"):
    st.session_state.analyzed = True

# 6. 분석이 시작되었을 때만 하단 결과 화면 노출
if st.session_state.analyzed:

    # 기초대사량 및 권장 칼로리 계산
    if gender == "남자":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    if activity == "거의 안 움직임":
        daily_calorie = bmr * 1.2
    elif activity == "
