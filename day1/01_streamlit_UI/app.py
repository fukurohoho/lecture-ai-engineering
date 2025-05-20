import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
import requests
import io
import textwrap

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="Streamlit デモ", layout="wide", initial_sidebar_state="expanded"
)

st.sidebar.header("ガイド")
st.sidebar.info("消費したいイーストの量を変更して、パンのレシピを確認してみよう。")

st.title("Streamlit 改善版デモ(おいしいパンの作り方)")
st.markdown("## 🍞パンを作ろう！🍞")
st.markdown("参考：https://recipe.cotta.jp/recipe.php?recipeid=00009570")

st.subheader("消費したいイーストの量からパンの分量を考える")
yearst_gram = st.slider("消費したいイーストの質量[g]", 0, 10, 3)

grams_dict = {}
grams_dict["小麦粉"] = yearst_gram / 3 * 200
grams_dict["塩"] = yearst_gram
grams_dict["砂糖"] = yearst_gram / 3 * 14
grams_dict["スキムミルク"] = yearst_gram * 4
grams_dict["水"] = yearst_gram / 3 * 136
grams_dict["バター"] = yearst_gram / 3 * 10

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 分量たち")
    st.table(pd.DataFrame(grams_dict, index=["質量[g]"]).T)

with col2:
    # 画像の表示
    st.markdown(
        """
    <style>
    .big-font {
        width: 100%;
    }
    </style>
    <h3>パンのイメージ</h3>
    """,
        unsafe_allow_html=True,
    )
    img = Image.open(
        io.BytesIO(
            requests.get(
                "https://www.cotta.jp/images/201312/12011727_529af2d72d45b.jpg"
            ).content
        )
    )
    st.image(img)

opinion_box = st.text_input("意見があればなんでも書き込んでください")
if st.button("送信"):
    st.success("問題なく送信されました！")
