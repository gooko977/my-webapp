import streamlit as st
import random

# ------------------------------
# 페이지 기본 설정
# ------------------------------
st.set_page_config(
    page_title="MBTI 여행지 추천 💕",
    page_icon="🧳",
    layout="centered",
)

# ------------------------------
# 귀여운 커스텀 CSS
# ------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe6f0 0%, #e6f0ff 50%, #fff9e6 100%);
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #ff6fa5;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #6f7fff;
        margin-top: 4px;
        margin-bottom: 30px;
    }
    .result-card {
        background-color: #ffffffcc;
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 8px 20px rgba(255, 111, 165, 0.25);
        text-align: center;
        margin-top: 20px;
        border: 3px dashed #ffb6d5;
    }
    .place-name {
        font-size: 30px;
        font-weight: 800;
        color: #ff4f9a;
        margin-bottom: 10px;
    }
    .place-desc {
        font-size: 17px;
        color: #555555;
        line-height: 1.6;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff9dc4, #ffd1a9);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 25px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(255, 157, 196, 0.5);
        transition: 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 14px rgba(255, 157, 196, 0.7);
    }
    div[data-baseweb="select"] {
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# MBTI별 여행지 데이터
# ------------------------------
mbti_data = {
    "INTJ": {
        "emoji": "🦉",
        "places": [
            {"name": "아이슬란드 🇮🇸", "desc": "고요한 자연 속에서 혼자만의 사색을 즐길 수 있는 신비로운 나라예요. 오로라를 보며 우주적인 생각에 잠겨보세요."},
            {"name": "스위스 알프스 🏔️", "desc": "계획적인 당신에게 딱 맞는, 정교하게 잘 짜인 트레킹 코스가 가득한 곳이에요."},
        ],
    },
    "INTP": {
        "emoji": "🧠",
        "places": [
            {"name": "일본 교토 ⛩️", "desc": "고요한 사찰과 정원에서 깊은 생각에 빠지기 좋은 지적인 여행지예요."},
            {"name": "영국 옥스퍼드 📚", "desc": "지식의 향기가 가득한 도시에서 호기심을 마음껏 채워보세요."},
        ],
    },
    "ENTJ": {
        "emoji": "🦁",
        "places": [
            {"name": "미국 뉴욕 🗽", "desc": "역동적이고 야망 넘치는 당신에게 완벽한 글로벌 비즈니스와 문화의 중심지예요."},
            {"name": "싱가포르 🌆", "desc": "효율적이고 세련된 도시에서 리더십 넘치는 여행을 즐겨보세요."},
        ],
    },
    "ENTP": {
        "emoji": "🎭",
        "places": [
            {"name": "태국 방콕 🛺", "desc": "예측 불가능한 매력이 가득한 활기찬 도시, 새로운 아이디어가 마구 떠오를 거예요!"},
            {"name": "브라질 리우데자네이루 🎉", "desc": "즉흥적이고 에너지 넘치는 당신과 찰떡궁합인 축제의 도시예요."},
        ],
    },
    "INFJ": {
        "emoji": "🌙",
        "places": [
            {"name": "포르투갈 리스본 🌅", "desc": "따뜻하고 감성적인 골목길에서 깊은 영감을 얻을 수 있는 곳이에요."},
            {"name": "인도 리시케시 🕉️", "desc": "명상과 요가로 내면을 들여다보기 좋은, 영혼이 맑아지는 여행지예요."},
        ],
    },
    "INFP": {
        "emoji": "🌸",
        "places": [
            {"name": "프랑스 파리 🗼", "desc": "낭만적이고 예술적인 감성이 가득한, 몽상가 INFP를 위한 도시예요."},
            {"name": "뉴질랜드 🐑", "desc": "동화 같은 자연 속에서 마음의 평화를 찾을 수 있는 힐링 여행지예요."},
        ],
    },
    "ENFJ": {
        "emoji": "🌟",
        "places": [
            {"name": "이탈리아 로마 🍝", "desc": "사람들과의 따뜻한 교류와 풍부한 역사가 공존하는 매력적인 도시예요."},
            {"name": "케냐 사파리 🦒", "desc": "생명력 넘치는 자연 속에서 사람들과 특별한 유대를 쌓아보세요."},
        ],
    },
    "ENFP": {
        "emoji": "🎈",
        "places": [
            {"name": "스페인 바르셀로나 🎨", "desc": "자유롭고 창의적인 에너지가 넘치는, 열정 가득한 ENFP에게 딱이에요!"},
            {"name": "호주 시드니 🏄", "desc": "다양한 사람들과 액티비티로 가득한 신나는 모험의 도시예요."},
        ],
    },
    "ISTJ": {
        "emoji": "🗂️",
        "places": [
            {"name": "독일 뮌헨 🍺", "desc": "체계적이고 안정적인 여행을 원하는 당신을 위한, 질서정연하고 전통 있는 도시예요."},
            {"name": "캐나다 밴쿠버 🍁", "desc": "안전하고 계획적인 일정으로 여유롭게 즐길 수 있는 곳이에요."},
        ],
    },
    "ISFJ": {
        "emoji": "🍵",
        "places": [
            {"name": "일본 교토 온천마을 ♨️", "desc": "따뜻하고 아늑한 분위기에서 몸과 마음을 편안하게 쉴 수 있는 곳이에요."},
            {"name": "오스트리아 잘츠부르크 🎻", "desc": "포근하고 정겨운 마을 풍경 속에서 힐링해보세요."},
        ],
    },
    "ESTJ": {
        "emoji": "📋",
        "places": [
            {"name": "미국 워싱턴 D.C. 🏛️", "desc": "체계적이고 역사적인 곳을 좋아하는 당신에게 완벽한 여행지예요."},
            {"name": "두바이 🏙️", "desc": "완벽하게 관리된 럭셔리한 도시에서 확실한 만족을 느껴보세요."},
        ],
    },
    "ESFJ": {
        "emoji": "🎀",
        "places": [
            {"name": "그리스 산토리니 🏖️", "desc": "사랑하는 사람들과 함께 따뜻한 추억을 쌓기 좋은 로맨틱한 섬이에요."},
            {"name": "체코 프라하 🏰", "desc": "동화 같은 풍경 속에서 다정한 사람들과 함께 걷기 좋은 곳이에요."},
        ],
    },
    "ISTP": {
        "emoji": "🛠️",
        "places": [
            {"name": "몽골 초원 🐎", "desc": "자유롭고 독립적인 당신을 위한 광활한 대자연 속 모험이 기다려요."},
            {"name": "칠레 파타고니아 🏔️", "desc": "손으로 직접 부딪히며 탐험하기 좋은 거친 자연이 매력적이에요."},
        ],
    },
    "ISFP": {
        "emoji": "🎨",
        "places": [
            {"name": "인도네시아 발리 🌺", "desc": "예술적이고 감각적인 당신에게 딱 맞는 아름답고 여유로운 섬이에요."},
            {"name": "모로코 마라케시 🕌", "desc": "화려한 색감과 감성이 가득한, 자유로운 영혼을 위한 도시예요."},
        ],
    },
    "ESTP": {
        "emoji": "🏍️",
        "places": [
            {"name": "미국 라스베가스 🎰", "desc": "화려하고 즉흥적인 액티비티가 가득한, 스릴을 즐기는 당신을 위한 곳!"},
            {"name": "필리핀 보라카이 🏄‍♂️", "desc": "짜릿한 해양 스포츠와 신나는 파티가 있는 활기찬 섬이에요."},
        ],
    },
    "ESFP": {
        "emoji": "🎪",
        "places": [
            {"name": "미국 마이애미 🌴", "desc": "화려하고 사교적인 당신을 위한 파티와 해변이 가득한 도시예요."},
            {"name": "멕시코 칸쿤 🎊", "desc": "밝은 에너지로 가득한, 즐거움이 넘치는 축제 같은 여행지예요."},
        ],
    },
}

mbti_list = list(mbti_data.keys())

# ------------------------------
# 헤더
# ------------------------------
st.markdown('<div class="main-title">🌈 MBTI 여행지 추천 🧳</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 MBTI에 딱 맞는 여행지를 찾아드릴게요 💖</div>', unsafe_allow_html=True)

st.write("")

# ------------------------------
# MBTI 선택
# ------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_mbti = st.selectbox(
        "✨ 당신의 MBTI를 선택해주세요 ✨",
        mbti_list,
        index=None,
        placeholder="MBTI를 골라보세요!",
    )

st.write("")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    recommend_clicked = st.button("💌 여행지 추천받기 💌", use_container_width=True)

# ------------------------------
# 결과 출력
# ------------------------------
if recommend_clicked:
    if selected_mbti is None:
        st.warning("먼저 MBTI를 선택해주세요! 🥺")
    else:
        info = mbti_data[selected_mbti]
        place = random.choice(info["places"])
        st.balloons()
        st.markdown(
            f"""
            <div class="result-card">
                <div style="font-size:50px;">{info['emoji']}</div>
                <div style="font-size:22px; color:#999; margin-bottom:10px;">{selected_mbti} 유형을 위한 추천 여행지</div>
                <div class="place-name">{place['name']}</div>
                <div class="place-desc">{place['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------
# 푸터
# ------------------------------
st.write("")
st.write("")
st.markdown(
    '<div style="text-align:center; color:#aaa; font-size:13px;">Made with 💕 by MBTI Travel Recommender</div>',
    unsafe_allow_html=True,
)
