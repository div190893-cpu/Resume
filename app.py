from pathlib import Path

import streamlit as st
from PIL import Image
import base64
import datetime

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Divyansh_Resume.pdf"
profile_pic_path = current_dir / "assets" / "profile.jpeg"

# --- PAGE CONFIG ---
PAGE_TITLE = "Digital CV | Divyansh"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- DARK THEME CSS (embedded) ---
DARK_CSS = """
:root{
  --bg:#0b1020;
  --card:#0f1724;
  --muted:#94a3b8;
  --accent:#60a5fa;
  --accent-2:#7c3aed;
  --glass: rgba(255,255,255,0.03);
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, var(--bg) 0%, #071028 100%);
}

.section-card{
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  padding: 18px;
  border-radius: 12px;
  box-shadow: 0 6px 18px rgba(2,6,23,0.6);
  color: #e6eef8;
  border: 1px solid rgba(255,255,255,0.03);
}

.profile-img{
  border-radius: 12px;
  border: 2px solid rgba(255,255,255,0.04);
}

.badge{
  display:inline-block;
  padding:6px 10px;
  margin:4px 4px 4px 0;
  border-radius:999px;
  background: linear-gradient(90deg,#4f46e5,#a78bfa);
  color: #ffffff !important;
  font-weight:600;
  font-size:13px;
}

.small-muted{ color: var(--muted); font-size:13px;}

a.link-dark{ color: var(--accent); text-decoration:none; font-weight:600}

/* hide Streamlit footer */
#MainMenu {visibility: hidden;} 
footer {visibility: hidden;}
"""

# inject CSS
st.markdown(f"<style>{DARK_CSS}</style>", unsafe_allow_html=True)

# helper to read file bytes
def get_file_download_link(file_path: Path, label: str="Download"):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f"data:application/octet-stream;base64,{b64}"
    return href

# --- PROFILE ---
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    try:
        profile_pic = Image.open(profile_pic_path)
        st.image(profile_pic, width=230)
    except Exception:
        st.empty()

with col2:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='margin:0 0 6px 0'>{'Divyansh'}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='small-muted'>Results-oriented Analytics Manager with expertise in data analysis, reporting automation, and insight generation. Proven ability to turn data into actionable business recommendations and drive process improvements.</div>", unsafe_allow_html=True)

    # contact + download
    cols = st.columns([1,1,1])
    with cols[0]:
        st.markdown(f"<div style='margin-top:10px'><strong>📫 Email</strong><br><a class='link-dark' href='mailto:Divyansh_19@yahoo.com'>Divyansh_19@yahoo.com</a></div>", unsafe_allow_html=True)
    with cols[1]:
        if resume_file.exists():
            href = get_file_download_link(resume_file)
            st.markdown(f"<div style='margin-top:10px'><strong>📄 Resume</strong><br><a href='{href}' download='{resume_file.name}' class='link-dark'>Download PDF</a></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='small-muted'>Resume PDF not found in assets/</div>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown(f"<div style='margin-top:10px'><strong>📅 Updated</strong><br><span class='small-muted'>{datetime.date.today().strftime('%b %d, %Y')}</span></div>", unsafe_allow_html=True)

    # social badges
    st.markdown("<div style='margin-top:12px'></div>", unsafe_allow_html=True)
    socials = {
        'Kaggle': 'https://www.kaggle.com/divyansh1908',
        'LinkedIn': 'https://www.linkedin.com/in/divyansh-ds19/',
        'GitHub': 'https://github.com/div190893-cpu',
        'WhatsApp': 'https://api.whatsapp.com/send/?phone=918090821315&text=Hello+Divyansh',
    }
    badges_html = ""
    icons = {
        'Kaggle': '📊',
        'LinkedIn': '💼',
        'GitHub': '🐙',
        'WhatsApp': '💬'
    }
    for k, v in socials.items():
        icon = icons.get(k, '')
        badges_html += f"<a class='badge' href='{v}' target='_blank'>{icon} {k}</a>"
    st.markdown(badges_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

st.write('')

# --- TWO-COLUMN LAYOUT: LEFT = Experience, Right = Skills & Projects ---
left, right = st.columns([2, 1], gap='large')

with left:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.subheader('Experience & Qualifications')
    st.markdown("""
- **Strong foundation** in Data Analysis, Statistical Methods, Forecasting, and Insight Generation.
- **Experienced** in working with large datasets, performing trend analysis, forecasting, and generating actionable insights for cross-functional teams.
- **Led** end-to-end analytics projects—data collection, cleaning, modeling, dashboarding, and stakeholder communication.
- **Skilled** at translating technical insights into clear business recommendations for senior leadership and procurement teams.
- **Familiar** with data governance, audit readiness, and compliance-driven analytics workflows.
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write('')
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.subheader('Work History')

    # Job: Associate Manager
    st.markdown("<strong>Associate Manager – Analytics & Software Asset Insights | HCLTECH, Lucknow</strong>", unsafe_allow_html=True)
    st.markdown("<span class='small-muted'>Jan 2025 – Present</span>", unsafe_allow_html=True)
    st.write('')
    st.markdown("""
- Led data-driven software asset lifecycle management using ServiceNow, achieving **98% asset data accuracy** across procurement and usage records.
- Analyzed license utilization and consumption trends to identify optimization opportunities, driving **12–18% annual cost savings**.
- Developed automated Power BI dashboards and ServiceNow reports, cutting manual reporting time by **40%** and improving visibility for leadership.
- Implemented workflow automation to reduce data discrepancies by **25%**, and supported internal/external audits to ensure **100% audit readiness**.
- Mentored and managed a team of analysts; coordinated with Finance, IT, Procurement, and Legal to align analytics with business objectives.
""", unsafe_allow_html=True)

    st.write('')
    # Job: Senior Software Engineer (condensed / analytics focused)
    st.markdown("<strong>Senior Software Engineer – Analytics Contributor | HCLTECH, Lucknow</strong>", unsafe_allow_html=True)
    st.markdown("<span class='small-muted'>Jan 2020 – Dec 2025</span>", unsafe_allow_html=True)
    st.write('')
    st.markdown("""
- Produced monthly analytical reports and automated Excel/SQL pipelines for stakeholder reporting.
- Built dashboards to communicate KPIs and supported data-driven resource allocation.
- Led initiatives to optimize software spend and compliance, contributing to **12–18% cost savings** through data analysis.
- Conducted periodic compliance reconciliations and improved reporting accuracy by **30%**.
""", unsafe_allow_html=True)

    st.write('')
    # Other roles
    st.markdown("<strong>Senior Data Analyst | in3corp</strong>", unsafe_allow_html=True)
    st.markdown("<span class='small-muted'>Feb 2019 – Dec 2019</span>", unsafe_allow_html=True)
    st.write('')
    st.markdown("""
- Wrote and optimized SQL scripts for complex analyses and report generation.
- Developed analytical databases and client deliverables; performed SAP-related research for client engagements.
""", unsafe_allow_html=True)

    st.write('')
    st.markdown("<strong>Data Analyst | in3corp</strong>", unsafe_allow_html=True)
    st.markdown("<span class='small-muted'>Jul 2015 – Feb 2019</span>", unsafe_allow_html=True)
    st.write('')
    st.markdown("""
- Extracted and analyzed data using SQL and Excel; automated reporting workflows and maintained KPI dashboards.
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.subheader('Hard Skills')
    st.markdown("""
- **Programming:** Python (Pandas, NumPy, scikit-learn, PySpark) • SQL • Advanced Excel
- **Visualization:** Power BI • Plotly • Streamlit • Tableau (basic)
- **Databases / Tools:** MySQL • ServiceNow Reporting • MS Access
- **Modeling:** Supervised & Unsupervised Learning • Forecasting • Predictive Analytics
- **Other:** Reporting Automation • Data Governance • Audit-ready Analytics
""", unsafe_allow_html=True)

    st.write('')
    st.subheader('Projects & Links')
    st.write('')
    # Projects (use your actual project links — placeholders below)
    projects = {
        "PhonePe Project (SQL + Python)": "https://github.com/div190893-cpu/PhonePe_Project",
        "Resume Repository": "https://github.com/div190893-cpu/Resume",
        "Luxury Housing Sales Analysis – Bengaluru": "https://github.com/div190893-cpu/Luxury-Housing-Sales-Analysis-Bengaluru"
    }
    for title, link in projects.items():
        st.markdown(f"- [{title}]({link})")

    st.write('')
    st.subheader('Education')
    st.markdown("**B.Tech, Computer Science | UPTU** — Passing Year: 2015")
    st.markdown("**Intermediate (PCM + Computer Science) | CBSE** — 2011")
    st.markdown("**Matriculation | U.P. Board** — 2009")

    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.write('')
st.markdown("<div class='small-muted' style='text-align:center; padding:18px;'>Built with Streamlit • © {}</div>".format(datetime.date.today().year), unsafe_allow_html=True)
