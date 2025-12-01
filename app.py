import streamlit as st
import numpy as np

st.title("🎓 US University Admission Prediction Dashboard")
st.write("根据学生的 GPA、托福、SAT、竞赛经历预测录取概率（简化版，无需模型文件）")

# 输入参数
gpa = st.slider("GPA（0.0 - 4.0）", 0.0, 4.0, 3.5)
toefl = st.slider("TOEFL（0 - 120）", 0, 120, 100)
sat = st.slider("SAT（0 - 1600）", 0, 1600, 1400)
awards = st.slider("竞赛奖项数量", 0, 10, 1)

# -------- 简单的模拟模型（可自行调整权重）--------
# 公式只是为了演示，你之后可以换成真正模型
score = (
    gpa * 0.4 +
    (toefl / 120) * 0.2 +
    (sat / 1600) * 0.3 +
    (awards * 0.1)
)

# 限制在 0 - 1 范围
prob = max(0, min(score / 4.0, 1))

# 显示结果
st.subheader(f"📈 录取概率：{prob*100:.2f}%")