import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Python CoffeeCo", layout="wide", initial_sidebar_state="expanded"
)

st.html(
    """
    <style>
        section:not([data-testid="stSidebar"]) .stPageLink p {
            font-size: 1.5rem;
            font-weight: 600;
        }
        .hero{
            justify-content:center;
            text-align:center;
        }
    </style>
    """
)

with st.container(border=True):
    st.html(
        """
        <div class="hero">
            <h1>Python CoffeeCo</h1>
            <h3>Independent coffee roasters on Snake Island.<br>
            Small batch. Ethically sourced. No nonsense.</h3>
        </div>
        """
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.page_link(
            "pages/products.py",
            label="Visit Our Online Store",
            use_container_width=True,
        )

st.divider()
st.markdown("### Our Branches")
st.caption("Visit us across Snake Island")
with st.container(border=True):
    df = pd.DataFrame(
        [
            {"lon": -46.6746, "lat": -24.4858},
            {"lon": -46.6749, "lat": -24.4810},
            {"lon": -46.6760, "lat": -24.4802},
        ]
    )
    st.map(df, zoom=12)


st.divider()
st.caption("Roasted with ❤️ and Python")
