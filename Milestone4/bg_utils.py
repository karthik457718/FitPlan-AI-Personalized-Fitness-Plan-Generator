# bg_utils.py  — Optimized for Hugging Face Spaces
# Place in project root (same folder as app.py)

import streamlit as st

def apply_bg(url: str = None, overlay: str = "rgba(0,0,0,0.50)") -> None:
    """
    Apply full-page background with overlay to Streamlit app.
    Optimized for Hugging Face Spaces deployment.
    
    Parameters:
        url (str): Image URL (Unsplash, etc.). Defaults to non-veg themed image.
        overlay (str): CSS rgba color for darkening overlay
    """
    
    # Default: Professional non-veg/protein food background
    if url is None:
        url = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1600&q=80&fit=crop"
    
    # Create CSS with maximum specificity and !important flags
    css = f"""
    <style>
    /* Maximum specificity background application */
    html, body {{
        width: 100% !important;
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background-image: url("{url}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
        background-color: #1a1a1a !important;
    }}
    
    body {{
        background-image: url("{url}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    
    .stApp {{
        background-image: linear-gradient(180deg, {overlay} 0%, rgba(0,0,0,0.22) 50%, {overlay} 100%), 
                          url("{url}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    
    /* Override Streamlit containers */
    [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}
    
    [data-testid="stMain"] {{
        background: transparent !important;
    }}
    
    div[class*="stApp"] {{
        background: transparent !important;
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)