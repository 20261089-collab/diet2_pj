import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="맞춤형 다이어트 도움 앱",
    page_icon="🥗",
    layout="centered"
)

# 음식 데이터
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

# 제목
st.title("🥗 맞춤형 다이어트 도움 앱")
st.caption("사용자 정보 기반 식단 및 운동 추천 시스템")

st.divider()

# 사용자 정보 입력
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

# 칼로리 계산 버튼
if st.button("✨ 사용자 분석 시작"):

    # 기초대사량 계산
    if gender == "남자":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # 활동량 반영
    if activity == "거의 안 움직임":
        daily_calorie = bmr * 1.2
    elif activity == "보통":
        daily_calorie = bmr * 1.55
    else:
        daily_calorie = bmr * 1.725

    # 목표 반영
    if goal == "감량":
        daily_calorie -= 300
    elif goal == "근육증가":
        daily_calorie += 300

    daily_calorie = int(daily_calorie)

    # 결과 출력
    st.success(f"{name}님의 하루 권장 칼로리는 약 {daily_calorie} kcal 입니다.")

    st.divider()

    # 맞춤 식단 추천
    st.header("🍱 맞춤형 추천 식단")

    recommended = []

    for food in foods:

        if allergy != "없음" and allergy in food:
            continue

        if dislike != "없음" and dislike in food:
            continue

        if foods[food]["type"] == food_style:
            recommended.append(food)

    if len(recommended) == 0:
        st.warning("조건에 맞는 식단이 부족해서 기본 식단을 추천합니다.")
        recommended = ["계란", "고구마", "샐러드"]

    for food in recommended:
        st.write(f"- {food}: {foods[food]['calorie']} kcal")

    st.divider()

    # 운동 추천
    st.header("🏃 맞춤형 운동 추천")

    exercise_time = st.slider(
        "하루 운동 가능 시간(분)",
        10,
        120,
        30
    )

    if goal == "감량":

        if exercise_time < 20:
            exercise = "빠르게 걷기 15분 + 스쿼트 20개"

        elif exercise_time < 40:
            exercise = "유산소 20분 + 스쿼트 30개 + 플랭크 1분"

        else:
            exercise = "러닝 30분 + 스쿼트 50개 + 플랭크 2분"

    elif goal == "근육증가":

        if exercise_time < 20:
            exercise = "스쿼트 30개 + 푸쉬업 15개"

        elif exercise_time < 40:
            exercise = "스쿼트 50개 + 푸쉬업 30개 + 런지 30개"

        else:
            exercise = "하체 근력운동 30분 + 상체 근력운동 30분"

    else:

        if exercise_time < 20:
            exercise = "가벼운 스트레칭 10분 + 산책 10분"

        elif exercise_time < 40:
            exercise = "산책 20분 + 전신 스트레칭 10분"

        else:
            exercise = "걷기 30분 + 요가 20분"

    st.info(f"추천 운동: {exercise}")

    st.divider()

    # 음식 기록
    st.header("🍽️ 오늘 먹은 음식 기록")

    selected_foods = st.multiselect(
        "먹은 음식을 선택하세요",
        list(foods.keys())
    )

    total = 0

    for food in selected_foods:
        total += foods[food]["calorie"]

    st.write(f"총 섭취 칼로리: {total} kcal")
    st.write(f"권장 칼로리: {daily_calorie} kcal")

    st.divider()

    # 피드백
    st.header("💬 맞춤 피드백")

    if total == 0:
        st.write("음식을 선택하면 피드백이 제공됩니다.")

    elif total > daily_calorie:
        st.error("오늘 권장 칼로리를 초과했어요.")
        st.write("내일은 저녁을 조금 가볍게 먹는 것을 추천해요.")

    elif total < daily_calorie - 500:
        st.warning("오늘 섭취량이 너무 적을 수 있어요.")
        st.write("단백질과 탄수화물을 균형 있게 챙겨 먹는 것을 추천해요.")

    else:
        st.success("오늘은 목표 칼로리에 잘 맞게 먹었어요!")

    if goal == "감량":
        st.write("고단백, 저칼로리 식단을 추천합니다.")

    elif goal == "근육증가":
        st.write("단백질 섭취를 충분히 하는 것이 좋아요.")

    else:
        st.write("현재 식사 균형을 유지하는 것이 좋아요.")