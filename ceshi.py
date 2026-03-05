import streamlit as st

# 页面基础配置（标题、图标、布局）
st.set_page_config(
    page_title="我的应用",  # 浏览器标签标题
    page_icon="📊",        # 标签图标（emoji或图片路径）
    layout="wide",         # 布局：wide（宽屏）/centered（居中）
    initial_sidebar_state="expanded"  # 侧边栏默认展开
)