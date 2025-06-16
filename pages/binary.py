import streamlit as st

st.set_page_config(page_title="이진 탐색 게임", page_icon="🎯")

st.title("🎯 이진 탐색 숫자 맞추기 게임")

# 상태 초기화
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "attempts" not in st.session_state:
    st.session_state.attempts = 1
if "done" not in st.session_state:
    st.session_state.done = False
if "last_action" not in st.session_state:
    st.session_state.last_action = None

# 응답에 따른 상태 변경
if st.session_state.last_action == "up":
    st.session_state.low = st.session_state.guess + 1
    st.session_state.attempts += 1
elif st.session_state.last_action == "down":
    st.session_state.high = st.session_state.guess - 1
    st.session_state.attempts += 1
elif st.session_state.last_action == "correct":
    st.session_state.done = True

# 범위 오류 확인
if st.session_state.low > st.session_state.high:
    st.error("잘못된 응답입니다. 범위가 뒤바뀌었어요.")
    if st.button("🔄 다시 시작"):
        st.session_state.clear()
    st.stop()

# 새 추측 계산
st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

# 결과 또는 추측 보여주기
if st.session_state.done:
    st.success(f"🎉 정답은 {st.session_state.guess}입니다! 총 {st.session_state.attempts}번 만에 맞췄어요.")
    st.balloons()
    if st.button("🔄 다시 시작"):
        st.session_state.clear()
else:
    st.subheader(f"🤖 제 추측: {st.session_state.guess}")
    st.write(f"현재 범위: {st.session_state.low} ~ {st.session_state.high}")
    st.write(f"시도 횟수: {st.session_state.attempts}")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 더 크다"):
            st.session_state.last_action = "up"
            st.experimental_rerun()

    with col2:
        if st.button("📉 더 작다"):
            st.session_state.last_action = "down"
            st.experimental_rerun()

    with col3:
        if st.button("✅ 정답!"):
            st.session_state.last_action = "correct"
            st.experimental_rerun()
