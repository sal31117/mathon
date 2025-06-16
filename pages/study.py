import streamlit as st
import time
from datetime import timedelta

st.set_page_config(page_title="Pomodoro 타이머", page_icon="⏰")

st.title("🍅 Pomodoro 타이머")
st.markdown("**25분 집중 + 5분 휴식** 주기로 학습 집중력을 높여보세요!")

# 초기 상태 설정
if "phase" not in st.session_state:
    st.session_state.phase = "집중"  # "집중" or "휴식"
if "running" not in st.session_state:
    st.session_state.running = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "duration" not in st.session_state:
    st.session_state.duration = 25 * 60  # 25분

# 단계 전환 함수
def switch_phase():
    if st.session_state.phase == "집중":
        st.session_state.phase = "휴식"
        st.session_state.duration = 5 * 60
    else:
        st.session_state.phase = "집중"
        st.session_state.duration = 25 * 60
    st.session_state.start_time = time.time()

# 시작 버튼 누르면 시간 기록
if st.button("▶️ 시작"):
    if not st.session_state.running:
        st.session_state.start_time = time.time()
        st.session_state.running = True

# 중지
if st.button("⏸ 중지"):
    st.session_state.running = False

# 초기화
if st.button("🔄 초기화"):
    st.session_state.running = False
    st.session_state.phase = "집중"
    st.session_state.duration = 25 * 60
    st.session_state.start_time = None

# 타이머 표시
if st.session_state.running and st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    remaining = int(st.session_state.duration - elapsed)
    
    if remaining <= 0:
        st.success(f"✅ {st.session_state.phase} 완료!")
        switch_phase()
        remaining = st.session_state.duration

    minutes, seconds = divmod(remaining, 60)
    st.subheader(f"⏱ 남은 시간: {minutes:02d}:{seconds:02d}")
    st.info(f"현재 단계: **{st.session_state.phase} 중**")

    # 반복적으로 새로고침해서 실시간 표시 (1초 간격)
    st.experimental_rerun()
else:
    st.subheader("⏱ 타이머가 멈춰 있습니다.")
    st.info(f"현재 단계: **{st.session_state.phase} 중**")
