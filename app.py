import streamlit as st
import db  # 우리가 만든 db.py를 불러옵니다!

# 앱 시작 시 DB 초기화 (db.py 안에 있는 함수 실행)
db.init_db()

# --- Streamlit UI 구성 ---
st.set_page_config(page_title="와이프를 위한 영어 선생님", page_icon="💖")
st.title("👍영어 학습앱👍")
st.caption("👩(A)와 👨(B)의 대화를 소리 내어 읽어보세요!")

# 1. 레벨 선택
level = st.selectbox("Step 1. 레벨을 선택하세요", ["초급 (Beginner)", "중급 (Intermediate)", "고급 (Advanced)"])

# 2. 주제 선택 (db.py에서 가져오기)
topics = db.get_topics_by_level(level)
selected_topic = st.selectbox("Step 2. 주제를 선택하세요", topics)

st.divider()

# 3. 대화문 표시
if st.button(f"'{selected_topic}' 대화 시작하기"):
    # db.py에서 내용 가져오기
    content = db.get_content_by_topic(level, selected_topic)

    if content:
        st.subheader(f"💬 {selected_topic} (Dialogue)")

        # 깔끔한 상자에 대화문 표시
        with st.container(border=True):
            # 통으로 된 글자를 줄바꿈(\n) 기준으로 잘라서 한 줄씩 꾸며줍니다.
            for line in content.split('\n'):
                line = line.strip() # 앞뒤 공백 제거

                # 빈 줄은 건너뛰기
                if not line:
                    continue

                # 👩 여자 대사: 주황색 + 굵게
                if line.startswith("👩"):
                    st.markdown(f"##### :orange[{line}]")

                # 👨 남자 대사: 파란색 + 굵게
                elif line.startswith("👨"):
                    st.markdown(f"##### :blue[{line}]")

                # (괄호) 한글 해석: 회색 + 작게
                elif line.startswith("("):
                    st.markdown(f":gray[{line}]")
                    st.write("") # 해석 밑에 약간의 여백 추가

                # 그 외
                else:
                    st.markdown(line)

        st.success("참 잘했어요! 다시 한 번 읽어볼까요? 👏")
    else:
        st.error("데이터를 불러오지 못했습니다.")

# 4. 연습장
st.divider()
st.text_area("📝 받아쓰기 연습장", placeholder="👩: Hello...\n(여기에 대화 내용을 직접 타이핑하며 연습해보세요)")