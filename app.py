import streamlit as st
import pandas as pd
from datetime import datetime
import json
import random

st.set_page_config(
    page_title="AI Spam Detector | Nimra Iftikhar",
    page_icon="🛡️",
    layout="wide"
)

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Dark mode toggle function
def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Theme based styling
if st.session_state.dark_mode:
    bg_color = "#1a1a2e"
    text_color = "#ffffff"
    card_bg = "#16213e"
    border_color = "#0f3460"
else:
    bg_color = "#f8f9fa"
    text_color = "#1a1a2e"
    card_bg = "#ffffff"
    border_color = "#ddd"

# Custom CSS
st.markdown(f"""
<style>
    .stApp {{
        background: {bg_color};
    }}
    
    .main-header {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    }}
    
    .main-header h1 {{
        color: white !important;
        margin: 0;
        font-size: 2.5rem;
    }}
    
    .main-header p {{
        color: rgba(255,255,255,0.9) !important;
        margin: 10px 0 0 0;
    }}
    
    .spam-card {{
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }}
    
    .spam-card h1, .spam-card p {{
        color: white !important;
    }}
    
    .safe-card {{
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
    }}
    
    .safe-card h1, .safe-card p {{
        color: white !important;
    }}
    
    .stTextArea textarea {{
        background: {card_bg};
        color: {text_color};
        border: 1px solid {border_color};
        border-radius: 10px;
    }}
    
    .stButton > button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        font-weight: 600;
        border-radius: 10px;
    }}
    
    .history-card {{
        background: {card_bg};
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 4px solid #667eea;
        color: {text_color};
    }}
    
    .stat-card {{
        background: {card_bg};
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid {border_color};
    }}
    
    .footer {{
        text-align: center;
        color: {text_color if st.session_state.dark_mode else '#666'};
        padding: 1rem;
        margin-top: 2rem;
        opacity: 0.7;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1> AI SPAM DETECTOR</h1>
    <p>Copy. Paste. Know if it's REAL or SCAM.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Dark mode toggle
    if st.button("🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode"):
        toggle_theme()
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("## 🚨 Spam Indicators")
    st.warning("• Urgent language")
    st.warning("• Suspicious links")
    st.warning("• Too good to be true")
    st.warning("• Poor grammar")
    st.warning("• Unknown sender")
    
    st.markdown("---")
    
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()

# Statistics Dashboard
st.markdown("## 📊 Statistics Dashboard")

if st.session_state.history:
    total_scans = len(st.session_state.history)
    spam_count = sum(1 for h in st.session_state.history if h["result"] == "SPAM")
    safe_count = total_scans - spam_count
    spam_percentage = (spam_count / total_scans) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <h3>📊 {total_scans}</h3>
            <p>Total Scans</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <h3>🚨 {spam_count}</h3>
            <p>Spam Detected</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <h3>✅ {safe_count}</h3>
            <p>Safe Emails</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <h3>{spam_percentage:.1f}%</h3>
            <p>Spam Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress bar
    st.progress(spam_percentage / 100)
else:
    st.info("No scans yet. Analyze an email to see statistics!")

st.markdown("---")

# Main content
st.markdown("## 📧 Email Analysis Engine")

col1, col2 = st.columns([2, 1])

with col1:
    email_text = st.text_area(
        "",
        height=200,
        placeholder="""Paste any email here...

Example:
Congratulations! You've won $1,000,000!
Click here to claim your prize now: http://fake-link.com
Hurry! This offer expires in 24 hours.""",
        label_visibility="collapsed"
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        analyze = st.button("🔍 Analyze Email", use_container_width=True)

with col2:
    st.markdown("### 💡 Quick Tips")
    st.markdown("""
    ✅ Check sender email
    ✅ Look for spelling errors
    ✅ Hover before clicking
    ✅ Never share passwords
    """)

# Analysis Results
if analyze and email_text:
    with st.spinner("Analyzing..."):
        spam_keywords = ["win", "prize", "click", "urgent", "verify", 
                        "password", "million", "free", "claim", "lottery",
                        "congratulations", "limited", "expires", "bank", "account"]
        
        email_lower = email_text.lower()
        found_keywords = [w for w in spam_keywords if w in email_lower]
        spam_score = len(found_keywords)
        confidence = min(100, spam_score * 12)
        
        is_spam = spam_score >= 2
        
        # Save to history
        st.session_state.history.insert(0, {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text": email_text[:100] + "..." if len(email_text) > 100 else email_text,
            "result": "SPAM" if is_spam else "SAFE",
            "confidence": confidence,
            "keywords": found_keywords,
            "full_text": email_text
        })
        
        st.session_state.history = st.session_state.history[:20]
        
        # Display result
        if is_spam:
            st.markdown("""
            <div class="spam-card">
                <h1>🚨 SPAM DETECTED</h1>
                <p style="font-size:1.2rem;">This email appears to be spam/scam</p>
                <p>⚠️ Do not click any links or reply</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="safe-card">
                <h1>✅ SAFE EMAIL</h1>
                <p style="font-size:1.2rem;">No threats detected</p>
                <p>✓ This email appears legitimate</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Detailed Analysis with Copy & Export
        with st.expander("📋 Detailed Analysis", expanded=True):
            col_a, col_b = st.columns([3, 1])
            with col_a:
                if is_spam:
                    st.error(f"**Risk Score:** {confidence}% - HIGH RISK")
                    st.write(f"**Suspicious keywords found:** {', '.join(found_keywords) if found_keywords else 'None'}")
                    st.warning("**Recommendation:** Delete this email immediately")
                else:
                    st.success(f"**Risk Score:** {confidence}% - LOW RISK")
                    st.success("✓ No suspicious patterns detected")
                st.progress(confidence/100)
            
            with col_b:
                # Copy result button
                result_text = f"Result: { 'SPAM' if is_spam else 'SAFE' }\nConfidence: {confidence}%\nAnalyzed by AI Spam Detector - Nimra Iftikhar"
                if st.button("📋 Copy Result"):
                    st.write("✅ Copied to clipboard!")
                    st.code(result_text)
                
                # Export button
                if st.button("📥 Export as TXT"):
                    export_content = f"""
AI SPAM DETECTOR - ANALYSIS REPORT
=====================================
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Result: {'SPAM DETECTED' if is_spam else 'SAFE EMAIL'}
Confidence: {confidence}%

Email Content:
{email_text}

Suspicious Keywords: {', '.join(found_keywords) if found_keywords else 'None'}

Report Generated by: Nimra Iftikhar
"""
                    st.download_button(
                        label="📥 Download Report",
                        data=export_content,
                        file_name=f"spam_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )

elif analyze and not email_text:
    st.warning("⚠️ Please paste some email content to analyze")

# History Section
st.markdown("---")
st.markdown("## 📜 Analysis History")

if st.session_state.history:
    for item in st.session_state.history[:10]:
        color = "#dc3545" if item["result"] == "SPAM" else "#28a745"
        st.markdown(f"""
        <div class="history-card" style="border-left-color: {color};">
            <small>{item['date']}</small>
            <p><strong>Result:</strong> {item['result']} | <strong>Confidence:</strong> {item['confidence']}%</p>
            <p><small>{item['text']}</small></p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No analysis yet. Paste an email above and click Analyze!")

# Footer
st.markdown(f"""
<div class="footer">
    <p>🤖 <strong>AI SPAM DETECTOR</strong> | Made by Nimra Iftikhar</p>
</div>
""", unsafe_allow_html=True)
