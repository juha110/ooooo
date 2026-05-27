import streamlit as st
import google.generativeai as genai
from datetime import datetime

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="공부 시간 추천 챗봇",
    page_icon="📚",
    layout="centered"
)

st.title("📚 공부 시간 추천 챗봇")
st.caption("과목별 공부 시간을 추천해주는 Gemini 챗봇")

# -----------------------------
# API 키 불러오기
# -----------------------------
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("❌ secrets.toml 에 GEMINI_API_KEY를 설정해주세요.")
    st.stop()

# Gemini 설정
genai.configure(api_key=GEMINI_API_KEY)

# 모델 생성
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 이전 채팅 출력
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 시스템 프롬프트
# -----------------------------
SYSTEM_PROMPT = """
너는 공부 계획을 도와주는 AI 챗봇이다.

사용자의 공부 과목, 목표, 시험 날짜, 현재 수준을 고려해서
과목별 추천 공부 시간을 알려줘.

답변 규칙:
- 표 형태로 정리
- 현실적인 공부 시간 제안
- 쉬는 시간도 포함
- 동기부여 한 줄 추가
- 한국어로 답변
"""

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("예: 수학 2시간, 영어 1시간 공부 계획 짜줘")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI 응답 생성
    with st.chat_message("assistant"):

        with st.spinner("공부 계획 생성 중..."):

            try:
                # 대화 기록 구성
                conversation_text = SYSTEM_PROMPT + "\n\n"

                for msg in st.session_state.messages:
                    role = "사용자" if msg["role"] == "user" else "AI"
                    conversation_text += f"{role}: {msg['content']}\n"

                # Gemini 호출
                response = model.generate_content(conversation_text)

                bot_reply = response.text

                # 응답 출력
                st.markdown(bot_reply)

                # 응답 저장
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })

            except Exception as e:
                error_message = f"""
❌ 오류가 발생했습니다.

오류 내용:
`{str(e)}`

잠시 후 다시 시도해주세요.
"""

                st.error(error_message)

                # 오류도 기록
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "오류가 발생했습니다."
                })

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:

    st.header("⚙️ 기능")

    if st.button("🗑️ 채팅 기록 초기화"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("""
### 사용 예시
- 수능 공부 계획 짜줘
- 토익 공부 시간 추천해줘
- 하루 5시간 공부 루틴 만들어줘
- 시험 2주 남았는데 계획 세워줘
""")

    st.divider()

    st.caption(f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M')}")import streamlit as st
import google.generativeai as genai
from datetime import datetime

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="공부 시간 추천 챗봇",
    page_icon="📚",
    layout="centered"
)

st.title("📚 공부 시간 추천 챗봇")
st.caption("과목별 공부 시간을 추천해주는 Gemini 챗봇")

# -----------------------------
# API 키 불러오기
# -----------------------------
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("❌ secrets.toml 에 GEMINI_API_KEY를 설정해주세요.")
    st.stop()

# Gemini 설정
genai.configure(api_key=GEMINI_API_KEY)

# 모델 생성
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 이전 채팅 출력
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 시스템 프롬프트
# -----------------------------
SYSTEM_PROMPT = """
너는 공부 계획을 도와주는 AI 챗봇이다.

사용자의 공부 과목, 목표, 시험 날짜, 현재 수준을 고려해서
과목별 추천 공부 시간을 알려줘.

답변 규칙:
- 표 형태로 정리
- 현실적인 공부 시간 제안
- 쉬는 시간도 포함
- 동기부여 한 줄 추가
- 한국어로 답변
"""

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("예: 수학 2시간, 영어 1시간 공부 계획 짜줘")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI 응답 생성
    with st.chat_message("assistant"):

        with st.spinner("공부 계획 생성 중..."):

            try:
                # 대화 기록 구성
                conversation_text = SYSTEM_PROMPT + "\n\n"

                for msg in st.session_state.messages:
                    role = "사용자" if msg["role"] == "user" else "AI"
                    conversation_text += f"{role}: {msg['content']}\n"

                # Gemini 호출
                response = model.generate_content(conversation_text)

                bot_reply = response.text

                # 응답 출력
                st.markdown(bot_reply)

                # 응답 저장
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })

            except Exception as e:
                error_message = f"""
❌ 오류가 발생했습니다.

오류 내용:
`{str(e)}`

잠시 후 다시 시도해주세요.
"""

                st.error(error_message)

                # 오류도 기록
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "오류가 발생했습니다."
                })

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:

    st.header("⚙️ 기능")

    if st.button("🗑️ 채팅 기록 초기화"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("""
### 사용 예시
- 수능 공부 계획 짜줘
- 토익 공부 시간 추천해줘
- 하루 5시간 공부 루틴 만들어줘
- 시험 2주 남았는데 계획 세워줘
""")

    st.divider()

    st.caption(f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
