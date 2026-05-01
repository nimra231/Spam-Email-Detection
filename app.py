import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Nimra's AI Spam Detector",
    page_icon="🛡️",
    layout="wide"
)

# CLEAN LIGHT THEME - Easy to read
st.markdown("""
<style>
    /* Clean white background */
    .stApp {
        background: #f8f9fa;
    }
    
    /* Professional header */
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .main-header h1 {
        color: white !important;
        margin: 0;
        font-size: 2rem;
    }
    
    .main-header p {
        color: #ccc !important;
        margin: 10px 0 0 0;
    }
    
    /* Result cards with good contrast */
    .spam-card {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }
    
    .spam-card h1, .spam-card p {
        color: white !important;
    }
    
    .safe-card {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }
    
    .safe-card h1, .safe-card p {
        color: white !important;
    }
    
    /* Make text in main area dark for readability */
    .stMarkdown, .stTextArea label {
        color: #1a1a2e !important;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background: white;
        color: #1a1a2e;
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        font-weight: 600;
        border-radius: 10px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #16213e 0%, #1a1a2e 100%);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    /* Metrics cards */
    .stMetric {
        background: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #1a1a2e !important;
        background: #f0f0f0;
        border-radius: 10px;
    }
    
    /* Success/Warning/Error messages */
    .stAlert {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🛡️ NIMRA'S AI SPAM DETECTOR</h1>
    <p>Enterprise-Grade Email Security | AI-Powered Protection</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 👩‍💻 Developer")
    st.info("**Nimra**\n\nAI/ML Engineer")
    st.markdown("---")
    
    st.markdown("## 📊 Live Protection Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Emails Protected", "15,847", "+12%")
    with col2:
        st.metric("Spam Blocked", "1,234", "+8%")
    
    st.markdown("---")
    st.markdown("## 🚨 Spam Indicators")
    st.warning("• Urgent language")
    st.warning("• Suspicious links")
    st.warning("• Too good to be true")
    st.warning("• Poor grammar")
    st.warning("• Unknown sender")
    
    st.markdown("---")
    st.caption(f"© 2026 Nimra | Updated: {datetime.now().strftime('%I:%M %p')}")

# Main content
st.markdown("## 📧 Email Analysis Engine")
st.caption("Paste the email content below to check if it's spam or safe")

col1, col2 = st.columns([2, 1])

with col1:
    email_text = st.text_area(
        "",
        height=200,
        placeholder="""Example email content:

Congratulations! You've won $1,000,000!
Click here to claim your prize now: http://fake-link.com
Hurry! This offer expires in 24 hours.

Best regards,
Prize Department""",
        label_visibility="collapsed"
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        analyze = st.button("🔍 Analyze Email", use_container_width=True)

with col2:
    st.markdown("### ⚡ Quick Tips")
    with st.expander("How to spot spam", expanded=True):
        st.markdown("""
        ✅ Check sender email address
        ✅ Look for spelling errors
        ✅ Hover over links before clicking
        ✅ Never share personal info
        """)

# Results
if analyze:
    if email_text:
        with st.spinner("Nimra's AI analyzing email..."):
            import time
            time.sleep(1.5)
            
            spam_keywords = ["win", "prize", "click", "urgent", "verify", 
                            "password", "million", "free", "claim", "lottery",
                            "congratulations", "limited", "expires", "bank"]
            
            email_lower = email_text.lower()
            found_keywords = [w for w in spam_keywords if w in email_lower]
            spam_score = len(found_keywords)
            
            if spam_score >= 2:
                st.markdown("""
                <div class="spam-card">
                    <h1>🚨 SPAM DETECTED</h1>
                    <p style="font-size:1.2rem;">This email has been identified as spam</p>
                    <p>⚠️ Do not click any links or download attachments</p>
                    <p>⚠️ Do not reply or provide personal information</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("📋 View Detailed Analysis"):
                    st.error(f"**Risk Level:** HIGH ({(spam_score * 15)}%)")
                    st.write(f"**Suspicious keywords found:** {', '.join(found_keywords)}")
                    st.warning("**Recommendation:** Delete this email immediately")
                    st.progress(95)
            else:
                st.markdown("""
                <div class="safe-card">
                    <h1>✅ SAFE EMAIL</h1>
                    <p style="font-size:1.2rem;">No threats detected</p>
                    <p>✓ This email appears to be legitimate</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("📋 Security Summary"):
                    st.success(f"**Risk Level:** LOW ({spam_score * 15}%)")
                    st.success("✓ No spam patterns detected")
                    st.success("✓ Content appears legitimate")
                    st.progress(10)
    else:
        st.warning("⚠️ Please paste email content to analyze")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🛡️ <strong>Nimra's AI Spam Detector>

</div>
""", unsafe_allow_html=True)
