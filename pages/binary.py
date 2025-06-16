import streamlit as st

st.set_page_config(page_title="이진 탐색 게임", page_icon="🔍")

st.title("🎯 이진 탐색 숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자 하나를 **마음속으로 생각**하세요!")
st.write("컴퓨터가 이진 탐색 알고리즘으로 그 숫자를 맞힐 거예요.")

# 초기 상태 설정
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if "attempts" not in st.session_state:
    st.session_state.attempts = 1
if "done" not in st.session_state:
    st.session_state.done = False

# 진행 중이면 현재 상태 출력
if not st.session_state.done:
    st.subheader(f"🤖 제 추측: **{st.session_state.guess}**")
    st.write(f"범위: {st.session_state.low} ~ {st.session_state.high}")
    st.write(f"시도 횟수: {st.session_state.attempts}회")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 더 크다"):
            st.session_state.low = st.session_state.guess + 1
            st.session_state.attempts += 1

    with col2:
        if st.button("📉 더 작다"):
            st.session_state.high = st.session_state.guess - 1
            st.session_state.attempts += 1

    with col3:
        if st.button("✅ 정답!"):
            st.success(f"🎉 맞혔습니다! 당신의 숫자는 {st.session_state.guess}입니다.")
            st.write(f"총 시도 횟수: {st.session_state.attempts}회")
            st.balloons()
            st.session_state.done = True

    # 업데이트된 guess
    if not st.session_state.done:
        if st.session_state.low > st.session_state.high:
            st.error("❗ 뭔가 잘못된 것 같아요. 다시 시작해주세요.")
            st.session_state.done = True
        else:
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

# 게임이 끝났을 때 재시작
if st.session_state.done:
    if st.button("🔄 다시 시작하기"):
        st.session_state.clear()
