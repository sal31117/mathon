import streamlit as st

st.set_page_config(page_title="이진 탐색 게임", page_icon="🎯")

st.title("🎯 이진 탐색 숫자 맞추기 게임")
st.markdown("""
마음속으로 **1부터 100 사이 숫자** 하나를 생각하세요.  
컴퓨터가 그 숫자를 **최대한 빨리** 맞혀볼게요!  
버튼으로 "더 크다 / 더 작다 / 정답!"만 눌러주면 돼요.
""")

# 세션 상태 초기화
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "attempts" not in st.session_state:
    st.session_state.attempts = 1
if "done" not in st.session_state:
    st.session_state.done = False

# 항상 최신 기준으로 추측 계산
if not st.session_state.done:
    if st.session_state.low > st.session_state.high:
        st.error("❌ 응답이 모순되어 더 이상 맞힐 수 없어요.")
        if st.button("🔄 다시 시작"):
            st.session_state.clear()
        st.stop()
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

# 진행 중 상태 출력
if not st.session_state.done:
    st.subheader(f"🤖 제 추측: **{st.session_state.guess}**")
    st.write(f"현재 범위: {st.session_state.low} ~ {st.session_state.high}")
    st.write(f"시도 횟수: {st.session_state.attempts}회")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 더 크다"):
            st.session_state.low = st.session_state.guess + 1
            st.session_state.attempts += 1
            st.rerun()

    with col2:
        if st.button("📉 더 작다"):
            st.session_state.high = st.session_state.guess - 1
            st.session_state.attempts += 1
            st.rerun()

    with col3:
        if st.button("✅ 정답!"):
            st.success(f"🎉 제가 맞혔습니다! 당신의 숫자는 **{st.session_state.guess}**입니다.")
            st.write(f"총 {st.session_state.attempts}번 만에 맞췄어요.")
            st.balloons()
            st.session_state.done = True

# 종료 상태
if st.session_state.done:
    if st.button("🔄 다시 시작"):
        st.session_state.clear()
