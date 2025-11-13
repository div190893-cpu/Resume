from pathlib import Path

import streamlit as st
from PIL import Image
#import matplotlib.pyplot as plt
import numpy as np

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir /"assets"/"Divyansh_Resume.pdf"
profile_pic = current_dir / "assets" / "profile.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Divyansh"
PAGE_ICON = ":wave:"
NAME = "Divyansh"
DESCRIPTION = """
Results-oriented Analytics Manager with expertise in data analysis, reporting automation, and insight generation. Proven ability to turn data into actionable business recommendations and drive process improvements.
"""
EMAIL = "Divyansh_19@yahoo.com"
SOCIAL_MEDIA = {
    "📉 Kaggle": "https://www.kaggle.com/divyansh1908",
    "💻 LinkedIn": "https://www.linkedin.com/in/divyansh-ds19/",
    "📊 GitHub": "https://github.com/div190893-cpu",
    "📞 Whatsapp": "https://api.whatsapp.com/send/?phone=918090821315&text=Hello+Divyansh%2C+I+saw+your+resume+and+would+like+to+connect.&type=phone_number&app_absent=0",
}
PROJECTS = {

    "🏆 Covid case study using folium": "https://www.kaggle.com/code/zuhaibbutt/covid-casestudy-using-folium",
    "🏆 Roman Urdu predition using machine learning models": "https://www.kaggle.com/code/zuhaibbutt/roman-urdu-prediction-with-test-value",
    "🏆 Dashboard on Tableau ":"https://public.tableau.com/app/profile/zuhaib3028/viz/lab12_16630698501100/Story1",
    "🏆 Common Disease Prediction using Machine Learning and NLP with Framework Flask" : "https://github.com/zuhaibbutt786/Ai-medical-chatbot", 
    "🏆 Simple Automatic-web-scraper":"https://github.com/zuhaibbutt786/automatic-web-scraper",
    "🏆 TelecomOptiXcel ":"https://github.com/zuhaibbutt786/telecom-sheets-app",
    "🏆 Laptop-price-prediction-with-streamlit ":"https://github.com/zuhaibbutt786/Laptop-price-prediction-with-streamlit",
    "🏆 Traffic-sign-classification-and-detection":"https://github.com/zuhaibbutt786/Traffic-sign-classification-and-detection",
   
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualification")
st.write(
    """
- ✔️Strong foundation in Data Analysis, Statistical Methods, Forecasting, and Insight Generation.
- ✔️Proficient in SQL, Excel, Data Visualization, Reporting Automation, and working knowledge of Python (if applicable—let me know if you want to include).
- ✔️Solid understanding of analytics lifecycle—data extraction, cleaning, transformation, exploration, and interpretation.
- ✔️Experience developing and presenting analytical insights to C-level and senior stakeholders for strategic decision-making.
- ✔️Knowledge of machine learning basics, predictive analysis, and applied analytics concepts (optional—confirm if you want to add more ML-specific points).
- ✔️Strong communication, leadership, and stakeholder management skills, ensuring alignment between data insights and business goals.
- ✔️Proven ability to manage multiple analytics initiatives, lead teams, and deliver measurable business impact.
- ✔️Familiar with data governance, audit readiness, and compliance-driven data analytics.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Panda, numpy , pyspark), SQL.
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Streamlit.
- 📚 Modeling: supervised and unsupervised learning models.
- 🗄️ Databases: MySQL,MS Access.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Associate Manager | HCLTECH, Lucknow **")
st.write("Dec' 24  - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Led data-driven software asset lifecycle management using ServiceNow, ensuring 98% asset data accuracy across procurement, deployment, and usage records.
- ►Translated complex analytical insights into clear business recommendations for senior leadership, influencing procurement strategy and vendor negotiations.
- ►Collaborated with Finance, IT, Procurement, and Legal to align software planning with budget cycles, compliance frameworks, and operational goals.
- ►Implemented workflow and reporting automation within ServiceNow, improving processing efficiency and reducing data discrepancies by 25%.
- ►Provided validated datasets and comprehensive documentation to support internal and external audits, ensuring 100% audit readiness.
- ►Forecasted future software and resource requirements using historical trends and usage patterns, enabling more accurate budget planning and contract renewals.
- ►Mentored internal teams on compliance standards, data interpretation, and effective usage of analytics dashboards, improving overall stakeholder adoption by 30%.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior Software Engineer | HCLTECH, Lucknow **")
st.write("Jan' 20 - Dec' 24")
st.write(
    """
- ► Produced monthly reports using advanced Excel spreadsheet functions.
- ► Created various Excel documents to assist with pulling metrics data and presenting  information to stakeholders for concise explanations of best placement for needed resources.
- ► Utilized data visualization tools to effectively communicate business insights.
- ► Extracted and interpreted data patterns to translate findings into actionable outcomes.
- ►Analyzed large datasets on license utilization and consumption trends, identifying underutilized assets and driving 12–18% annual cost savings through optimization recommendations.
- ►Developed automated dashboards and reports that improved visibility into spend, compliance gaps, and usage patterns, reducing manual reporting efforts by 40%.
- ►Conducted periodic license compliance audits, reconciling entitlements vs. consumption and helping reduce audit exposure by 30%.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Senior Data Analyst | in3corp**")
st.write("Feb' 19 - Dec' 19")
st.write("""
- ► Write and optimize SQL scripts for data analysis and report generation.
- ► Identify and resolve data discrepancies and errors using advanced SQL queries.
- ► Develop new analytical methodologies and queries to recover revenue and enhance client profitability.
- ► Advise clients on efficient data recording and transaction management practices.
- ► Contribute to analyst performance reviews and provide inputs for professional growth plans (PGPs).
- ► Prepare, write, and present formal client deliverables, insights, and reports.
- ► Build and maintain analytical databases from complex financial and operational data sources.
- ► Conduct research and analysis on client SAP systems to support data-driven decisions.

""")

# --- JOB 4
st.write('\n')
st.write("🚧", "**Data Analyst | in3corp**")
st.write("Jul' 15 - Feb' 19")
st.write(
    """
- ► Extract and analyze data using SQL queries and advanced Excel functions.
- ► Develop and maintain data reports, dashboards, and KPIs.
- ► Automate data processing and reporting workflows.
- ► Identify and interpret data trends and business insights.
- ► Ensure data quality, accuracy, and consistency across systems.
"""
)


# --- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- Edu 1
st.write('\n')
st.write("📚", "**B.Tech| UPTU | Computer Science**")
st.write("Passing Year: 2015")


# --- Edu 2
st.write('\n')
st.write("📚", "**Intermediate | CBSE Board| PCM + Computer Science**")
st.write("Passing Year: 2011")


# --- Edu 3
st.write('\n')
st.write("📚", "**Matriculation | U.P.Board*")
st.write("Passing Year: 2009")





# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

    
    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)    
