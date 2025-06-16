import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="공부 시간 기록기", page_icon="📚")

st.title("📚 공부 시간 기록 시각화기")

# 초기화
if "log" not in st.session_state:
    st.session_state.log = []
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# 시작 버튼
if st.button("▶️ 공부 시작"):
    st.session_state.start_time = datetime.datetime.now()
    st.success(f"공부 시작: {st.session_state.start_time.strftime('%H:%M:%S')}")

# 종료 버튼
if st.button("⏸ 공부 종료"):
    if st.session_state.start_time is not None:
        end_time = datetime.datetime.now()
        duration = (end_time - st.session_state.start_time).total_seconds() / 60  # 분 단위
        st.session_state.log.append({
            "날짜": datetime.datetime.now().strftime("%Y-%m-%d"),
            "시작": st.session_state.start_time.strftime("%H:%M:%S"),
            "종료": end_time.strftime("%H:%M:%S"),
            "공부 시간 (분)": round(duration, 2)
        })
        st.success(f"⏱ 공부 종료! {round(duration, 2)}분 공부했어요.")
        st.session_state.start_time = None
    else:
        st.warning("공부 시작을 먼저 눌러주세요!")

# 기록 보기
if st.session_state.log:
    df = pd.DataFrame(st.session_state.log)
    st.subheader("📝 오늘의 공부 기록")
    st.dataframe(df)

    # 누적 시간 계산
    total = df["공부 시간 (분)"].sum()
    st.metric("📊 오늘 총 공부 시간", f"{round(total, 1)}분")

    # 시각화
    chart_data = df.groupby("날짜")["공부 시간 (분)"].sum().reset_index()
    st.subheader("📈 날짜별 공부 시간")
    st.line_chart(chart_data.set_index("날짜"))
