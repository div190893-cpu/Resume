import streamlit as st
from PIL import Image

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="Divyansh | Data Analyst Resume",
    page_icon="💼",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            font-family: 'Inter', sans-serif;
            color: #333333;
        }

        /* Left Sidebar */
        .left-column {
            background-color: #e9ecef;
            padding: 30px;
            border-radius: 10px;
        }

        /* Section Titles */
        h2 {
            color: #004d40;
            border-bottom: 2px solid #004d40;
            padding-bottom: 5px;
            margin-top: 25px;
        }

        h3 {
            color: #004d40;
            margin-top: 20px;
            margin-bottom: 8px;
        }

        a {
            color: #004d40;
            text-decoration: none;
            font-weight: 500;
        }

        a:hover {
            color: #00796b;
        }

        .contact-icon {
            margin-right: 8px;
        }

        .small-text {
            font-size: 14px;
            color: #444444;
        }

        ul {
            margin-top: 0;
            padding-left: 20px;
        }

        .project-title {
            font-weight: 600;
        }

        hr {
            border: 0.5px solid #d0d0d0;
            margin: 1.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# LAYOUT (Two Columns)
# =========================
col1, col2 = st.columns([1, 2], gap="large")

# ---------- LEFT COLUMN ----------
with col1:
    st.markdown("<div class='left-column'>", unsafe_allow_html=True)

    # Profile Photo
    img = Image.open("assets/profile.jpeg")
    st.image(img, width=180)

    st.markdown("## Divyansh")
    st.markdown("_Data Analyst_")

    st.markdown("📧 **Divyansh_19@yahoo.com**")
    st.markdown("📞 **8090821315**")
    st.markdown("📍 Lucknow, U.P")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/divyansh-ds19)")
    st.markdown("[GitHub](https://github.com/div190893-cpu)")

    st.markdown("---")

    st.subheader("Profile")
    st.write("""
    Data Analyst with a passion for using data to drive business insights and efficiency. 
    Skilled in Python, SQL, Power BI, and data visualization. 
    Strong analytical mindset and detail-oriented approach to solving real-world problems.
    """)

    st.markdown("---")

    st.subheader("Education")
    st.write("""
    **B.Tech in Computer Science**  
    Dr. A.P.J. Abdul Kalam Technical University, 2015
    """)
    
    st.write("""
    **Higher Secondary with PCM & Computer Science**  
    Central Board of Secondary Education, 2011
    """)
    
    st.write("""
    **Marticulation**  
    U.P. Board, 2009
    """)

    st.markdown("---")

    with open("assets/Divyansh_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Divyansh_Resume.pdf",
        mime="application/pdf"
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------- RIGHT COLUMN ----------
with col2:
    st.markdown("## Skills")
    st.write("""
    **Python** (Pandas, NumPy, Matplotlib), 
    **SQL** (Ms Access, MySQL),  
    **Excel / Google Sheets** (Pivot Tables, VLOOKUP),  
    **Power BI / Streamlit** (Dashboard Creation, Data Visualization),  
    **Statistical Analysis** (Hypothesis Testing, A/B Testing)
    """)

    st.markdown("## Projects")

    st.markdown("### PhonePe Pulse Data Analysis")
    st.write("""
    - Built a **data pipeline** using Python and Power BI to visualize transaction data.  
    - Extracted insights into **digital payment adoption and regional trends**.  
    - Improved dashboard loading speed by 30% with optimized queries.  
    **Key Skills:** Python, Pandas, Power BI, Data Visualization.
    """)

    st.markdown("### Real Estate Market Analysis")
    st.write("""
    - Conducted **EDA** on Bangalore housing data to identify key price influencers.  
    - Built an interactive **Power BI dashboard** with filterable insights.  
    - Derived metrics on amenity score, micro-market impact, and location-based trends.  
    **Key Skills:** Power BI, SQL, Excel, EDA.
    """)

    st.markdown("### Sales Insights Dashboard")
    st.write("""
    - Designed a **KPI dashboard** for sales performance tracking.  
    - Analyzed regional trends and customer purchasing behavior.  
    - Enabled data-driven decision-making through automated Power BI reports.  
    **Key Skills:** Power BI, SQL, Excel.
    """)

    st.markdown("## Certifications")
    st.write("""
    - Google Data Analytics (Coursera)  
    - Power BI for Business Analytics  
    - Python for Data Science
    """)

    st.markdown("## Achievements")
    st.write("""
    - Increased data reporting efficiency by **40%** through process automation.  
    - Recognized for building **self-service BI dashboards** for senior management.
    """)

# ---------- FOOTER ----------
st.write("---")
st.caption("© 2025 Divyansh | Built with Streamlit | Inspired by FlowCV layout")
