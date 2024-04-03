import streamlit as st
from streamlit.components.v1 import html

# 토스 결제 위젯 스크립트 삽입을 위한 HTML 코드
toss_payment_widget_html = """
<head>
<meta charset="utf-8" />
<script src="https://js.tosspayments.com/v1/payment-widget"></script>
</head>
"""

# Streamlit 앱에 HTML 삽입
html(toss_payment_widget_html, height=0)  # 높이는 실제로 표시할 내용이 없기 때문에 0으로 설정
