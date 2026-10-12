from datetime import datetime
import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="🔮 오늘의 운세 보기", page_icon="✨", layout="centered"
)

# 12지신 띠 리스트
zodiac_signs = [
    "쥐띠",
    "소띠",
    "호랑이띠",
    "토끼띠",
    "용띠",
    "뱀띠",
    "말띠",
    "양띠",
    "원숭이띠",
    "닭띠",
    "개띠",
    "돼지띠",
]

# 운세 데이터 풀 (다양한 조합을 위한 템플릿)
general_fortunes = [
    "생각지도 못한 행운이 찾아오는 하루입니다. 주변 사람들에게 마음을 열어보세요.",
    "작은 노력이 큰 결실로 이어지는 기분 좋은 날입니다. 도전하는 것을 두려워하지 마세요.",
    "주변의 조언을 경청하면 큰 이득을 볼 수 있습니다. 오늘은 한 발 양보하는 미덕이 필요해요.",
    "에너지가 넘치는 하루입니다! 미루어두었던 일을 처리하기에 가장 좋은 타이밍입니다.",
    "마음의 여유를 갖고 차분하게 주변을 둘러보세요. 소소한 행복을 발견할 수 있습니다.",
    "귀인이 나타나 당신을 도와줄 수 있는 운수 좋은 날입니다.",
]

wealth_fortunes = [
    "재물운이 상승 곡선을 그리고 있습니다. 뜻밖의 소소한 수입이 생길 수 있어요.",
    "지갑을 열기 전에 한 번 더 고민해 보는 지혜가 필요합니다. 불필요한 지출을 줄이세요.",
    "안정적인 재정 상태가 유지됩니다. 투자나 계약은 오늘 하루 신중을 기하는 것이 좋습니다.",
    "급작스러운 금전 거래보다는 저축과 관리에 집중하는 것이 유리한 하루입니다.",
]

lucky_colors = ["빨간색", "파란색", "초록색", "노란색", "보라색", "흰색", "검은색"]

# UI 디자인 시작
st.markdown(
    "<h1 style='text-align: center; color: #6C63FF;'>🔮 오늘의 운세</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: gray;'>자신의 띠를 선택하고 오늘의 행운을 확인해 보세요!</p>",
    unsafe_allow_html=True,
)
st.write("---")

# 오늘 날짜 표시
today_str = datetime.now().strftime("%Y년 %m월 %d일")
st.subheader(f"📅 {today_str} 운세")

# 띠 선택 셀렉트박스
selected_zodiac = st.selectbox("당신의 띠를 선택해주세요:", zodiac_signs)

# 운세 확인 버튼
if st.button("✨ 운세 확인하기", use_container_width=True):
    # 매번 누를 때마다 띠 이름에 고유 시드를 주거나 랜덤으로 결과 출력
    # (매번 새로고침/클릭 시 달라지도록 random 사용)
    gen_fortune = random.choice(general_fortunes)
    wealth_fortune = random.choice(wealth_fortunes)
    lucky_num = random.randint(1, 45)
    lucky_col = random.choice(lucky_colors)

    st.success(f"🎉 **{selected_zodiac}**의 오늘의 운세가 도착했습니다!")

    # 결과를 카드 형태로 깔끔하게 출력
    st.markdown(
        f"""
        ### 🌟 총운
        > {gen_fortune}

        ### 💰 금전운
        > {wealth_fortune}

        ---
        🍀 **오늘의 행운 포인트**
        - **행운의 숫자:** `{lucky_num}`
        - **행운의 색상:** `{lucky_col}`
        """
    )
    st.balloons()  # 축하 효과 애니메이션