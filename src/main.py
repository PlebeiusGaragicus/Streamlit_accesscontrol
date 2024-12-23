import os
import pathlib
from PIL import Image

import streamlit as st

STATIC_PATH = pathlib.Path(__file__).parent.parent / "static"

def cmp_header():
    im = Image.open(os.path.join(STATIC_PATH, "favicon.ico"))
    st.set_page_config(
        # page_title="DEBUG!" if os.getenv("DEBUG", False) else "NOS4A2",
        page_title="plebtool!",
        # page_icon=os.path.join(STATIC_PATH, "favicon.ico"),
        page_icon=im,
        layout="wide",
        initial_sidebar_state="auto",
    )

    # column_fix()
    # center_text("p", "🗣️🤖💬", size=60) # or h1, whichever


from src.common import (
    is_init,
    get,
    cprint,
    Colors,
)

def main_page():
    ip_addr = st.context.headers.get('X-Forwarded-For', "?")
    user_agent = st.context.headers.get('User-Agent', "?")
    lang = st.context.headers.get('Accept-Language', "?")
    # print(f"RUNNING for IP address: {ip_addr}")
    # cprint("\n---> RERUN! <---\n", Colors.YELLOW)
    # cprint(f"RUNNING for IP address: {ip_addr}", Colors.YELLOW)
    cprint(f"RUNNING for: {ip_addr} - {lang} - {user_agent}", Colors.YELLOW)

    cmp_header()

    st.sidebar.header("", divider="rainbow")

    if os.getenv("DEBUG"):
        with st.sidebar:
            st.write(":orange[DEBUG]")
            st.write( st.context.cookies )
            st.write( st.context.headers )
    # else:
    #     st.write(":orange[PRODUCTION]")

    # st.write(f"The Secret is: {os.getenv('SECRET')}")

    st.write("not found")
