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
    cprint("\n---> RERUN! <---\n", Colors.YELLOW)
    # print("RUNNING")

    cmp_header()

    if os.getenv("DEBUG"):
        st.write(":orange[DEBUG]")
    else:
        st.write(":orange[PRODUCTION]")


    st.write("hello, there!")
    st.sidebar.header("", divider="rainbow")


    st.write( st.context.cookies )
    st.write( st.context.headers )

    # st.write()
