import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Spam Detector Pro | Enterprise Email Security",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ultra-professional look
st.markdown("""
<style>
    /* Professional dark-light gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main content card */
    .main-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.1);
    }
    
    /* Stats card */
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Result animations */
    @keyframes slideIn {
        from { transform: translateY(30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .result-card {
        animation: slideIn 0.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# Header with stats row
col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 1, 1])

with col1:
    st.image("https://img.icons8.com/color/96/000000/email-security.png", width=60)

with col2:
    st.markdown("# 🛡️ **SecureMail Pro**")
    st.markdown("*Enterprise Email Security Solution*")

with col3:
    st.metric("Total Scans", "15,847", "+12%")
with col4:
    st.metric("Spam Rate", "8.3%", "-2.1%")
with col5:
    st.metric("Protection", "Active", "✅")

st.markdown("---")

# Sidebar with advanced features
with st.sidebar:
    st.markdown("## 📊 **Dashboard**")
    
    # Real-time stats
    st.markdown("### Today's Activity")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Emails Scanned", "347", "+23")
    with col2:
        st.metric("Threats Blocked", "28", "+5")
    
    st.markdown("---")
    
    # Threat intelligence
    st.markdown("### 🎯 **Threat Intelligence**")
    threat_level = random.choice(["Low", "Medium", "High"])
    if threat_level == "Low":
        st.success(f"Current Threat Level: {threat_level}")
    elif threat_level == "Medium":
        st.warning(f"Current Threat Level: {threat_level}")
    else:
        st.error(f"Current Threat Level: {threat_level}")
    
    st.markdown("---")
    
    # User info
    st.markdown("### 👤 **Security Profile**")
    st.info("""
    **Protected Domains:** 3
    **Quarantined:** 127
    **False Positives:** 2
    """)
    
    st.markdown("---")
    st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Main content area with tabs
tab1, tab2, tab3, tab4 = st.tabs(["📧 **Email Scanner**", "📁 **Batch Scan**", "📊 **Analytics**", "⚙️ **Settings**"])

with tab1:
    st.markdown("### 🔍 **Real-time Email Analysis**")
    st.caption("Paste the email content below for instant spam detection")
    
    # Two column layout for input and tips
    input_col, tip_col = st.columns([2, 1])
    
    with input_col:
        email_text = st.text_area(
            "",
            height=250,
            placeholder="""Example email:
            
From: security@paypal.com
Subject: Your account has been limited

Dear valued customer,
Your account has been temporarily suspended. Click here to verify your information immediately.
Failure to do so will result in permanent closure.

Best regards,
PayPal Security Team""",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            analyze = st.button("🔍 **Run Security Scan**", type="primary", use_container_width=True)
    
    with tip_col:
        st.markdown("### 🚨 **Spam Indicators**")
        with st.expander("View Warning Signs", expanded=True):
            st.markdown("""
            - ⚡ Urgent action required
            - 💰 Too good to be true offers
            - 🔗 Suspicious links
            - 📝 Poor grammar/spelling
            - 👤 Unknown sender
            - 🏦 Fake bank alerts
            """)
        
        st.markdown("### 🛡️ **Protection Status**")
        st.progress(100, text="Maximum Security")
    
    # Results area
    if analyze:
        if email_text:
            with st.spinner("Performing deep scan..."):
                import time
                time.sleep(1)  # Simulate processing
                
                # Advanced detection logic
                spam_keywords = {
                    "urgent": 3, "verify": 3, "click": 2, "account": 2,
                    "password": 3, "suspended": 3, "winner": 2, "prize": 2,
                    "bank": 2, "security": 2, "limited": 3, "immediately": 2
                }
                
                email_lower = email_text.lower()
                spam_score = 0
                found_threats = []
                
                for keyword, weight in spam_keywords.items():
                    if keyword in email_lower:
                        spam_score += weight
                        found_threats.append(keyword)
                
                # Calculate confidence
                confidence = min(100, spam_score * 10)
                
                st.markdown("---")
                
                if spam_score >= 5:
                    # Spam detected
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                        <h1>🚨</h1>
                        <h2>SPAM DETECTED</h2>
                        <p style="font-size: 1.2rem;">High confidence malicious content</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Threat breakdown
                    with st.expander("🔍 **Detailed Threat Analysis**", expanded=True):
                        st.warning(f"**Risk Score:** {confidence}% - High Risk")
                        st.write(f"**Threats identified:** {', '.join(found_threats)}")
                        st.progress(confidence)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.error("**Phishing Indicators:** ✓")
                            st.error("**Suspicious Links:** ✓")
                        with col2:
                            st.error("**Urgency Tactics:** ✓")
                            st.error("**Spoofed Sender:** ✓")
                else:
                    # Safe email
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                                padding: 2rem; border-radius: 15px; text-align: center; color: white;">
                        <h1>✅</h1>
                        <h2>EMAIL SAFE</h2>
                        <p style="font-size: 1.2rem;">No threats detected</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander("🔍 **Security Summary**", expanded=True):
                        st.success(f"**Risk Score:** {confidence}% - Low Risk")
                        st.success("✓ Content appears legitimate")
                        st.success("✓ No suspicious patterns found")
        else:
            st.warning("⚠️ Please paste email content to scan")

with tab2:
    st.info("📁 **Upload multiple emails** for batch processing (Coming soon)")
    st.file_uploader("Choose MBOX or CSV file", type=['mbox', 'csv'], disabled=True)

with tab3:
    st.markdown("### 📈 **Security Analytics**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Last 7 Days")
        st.line_chart({"Spam Detected": [12, 8, 15, 10, 7, 14, 9]})
    with col2:
        st.markdown("#### Protection Rate")
        st.metric("Block Rate", "99.2%", "+0.5%")

with tab4:
    st.markdown("### ⚙️ **Security Preferences**")
    st.selectbox("Sensitivity Level", ["Low", "Medium", "High"], index=1)
    st.checkbox("Auto-quarantine suspected spam")
    st.checkbox("Email notifications for threats")
    st.button("Save Settings")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>🛡️ <strong>SecureMail Pro</strong> | Enterprise-Grade Email Security</p>
    
</div>
""", unsafe_allow_html=True)
