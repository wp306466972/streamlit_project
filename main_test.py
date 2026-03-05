import streamlit as st

# 页面标题
st.title("我的第一个 Streamlit 网页应用")
# 交互组件
name = st.text_input("请输入你的名字")
if name:
    st.write(f"你好，{name}！这个页面已经部署到网上了～")