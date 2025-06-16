import streamlit as st
import time

st.set_page_config(page_title="Pomodoro 타이머", page_icon="⏰")

st.title("🍅 Pomodoro 타이머")
st.markdown("**25분 집중 + 5분 휴식** 주기로 학습 집중력을 높여보세요!")

# 상태 초기화
if "phase" not in st.session_state:
    st.session_state.phase = "집중"
if "duration" not in st.session_state:
    st.session_state.duration = 25 * 60
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining" not in st.session_state:
    st.session_state.remaining = st.session_state.duration

# 단계 전환 함수
def switch_phase():
    if st.session_state.phase == "집중":
        st.session_state.phase = "휴식"
        st.session_state.duration = 5 * 60
    else:
        st.session_state.phase = "집중"
        st.session_state.duration = 25 * 60
    st.session_state.remaining = st.session_state.duration

# 버튼 인터페이스
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ 시작"):
        st.session_state.running = True

with col2:
    if st.button("⏸ 중지"):
        st.session_state.running = False

with col3:
    if st.button("🔄 초기화"):
        st.session_state.running = False
        st.session_state.phase = "집중"
        st.session_state.duration = 25 * 60
        st.session_state.remaining = st.session_state.duration

# 타이머 표시
timer_placeholder = st.empty()
status_placeholder = st.empty()

if st.session_state.running:
    while st.session_state.running and st.session_state.remaining > 0:
        mins, secs = divmod(st.session_state.remaining, 60)
        timer_placeholder.subheader(f"⏱ 남은 시간: {mins:02d}:{secs:02d}")
        status_placeholder.info(f"현재 단계: **{st.session_state.phase} 중**")
        time.sleep(1)
        st.session_state.remaining -= 1
        st.experimental_rerun()  # Streamlit 앱 구조상 여기는 써야 함
else:
    mins, secs = divmod(st.session_state.remaining, 60)
    timer_placeholder.subheader(f"⏱ 남은 시간: {mins:02d}:{secs:02d}")
    status_placeholder.info(f"현재 단계: **{st.session_state.phase} 중**")

# 종료 시
if st.session_state.remaining == 0:
    st.success(f"✅ {st.session_state.phase} 완료!")
    switch_phase()

