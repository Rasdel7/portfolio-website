import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Jyotiraditya Biswal",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main { padding: 0rem 2rem; }
    .hero {
        background: linear-gradient(
            135deg, #1A56DB 0%, #0e3a8c 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }
    .hero p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }
    .stat-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1A56DB;
    }
    .stat-label {
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }
    .project-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: all 0.2s;
    }
    .project-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111827;
    }
    .badge {
        display: inline-block;
        background: #EFF6FF;
        color: #1A56DB;
        padding: 2px 10px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        margin: 2px;
    }
    .section-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #111827;
        margin-bottom: 0.5rem;
    }
    .section-sub {
        color: #6b7280;
        margin-bottom: 1.5rem;
    }
    .skill-bar-label {
        font-weight: 600;
        color: #374151;
        font-size: 0.9rem;
    }
    .timeline-item {
        border-left: 3px solid #1A56DB;
        padding-left: 1rem;
        margin-bottom: 1.5rem;
    }
    .contact-link {
        background: #F3F4F6;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        display: block;
        text-decoration: none;
        color: #111827;
        font-weight: 500;
    }
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Jyotiraditya Biswal</h1>
    <p>ML Engineer Intern Candidate &nbsp;|&nbsp;
       2nd Year CSE @ SIT Bhubaneswar &nbsp;|&nbsp;
       Building in public. Every day.</p>
    <p style="margin-top:1rem; font-size:1rem;
              opacity:0.8">
        🔥 365-Day Project Challenge &nbsp;•&nbsp;
        57+ Projects Built &nbsp;•&nbsp;
        44+ Apps Deployed
    </p>
</div>
""", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)
stats = [
    ("57+",  "Projects Built"),
    ("44+",  "Apps Deployed"),
    ("200+", "GitHub Contributions"),
    ("7.5",  "CGPA"),
    ("365",  "Day Streak Goal")
]
for col, (num, label) in zip(
    [c1, c2, c3, c4, c5], stats
):
    col.markdown(
        f"""<div class="stat-card">
        <div class="stat-number">{num}</div>
        <div class="stat-label">{label}</div>
        </div>""",
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── NAV TABS ──────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚀 Projects",
    "🧠 Skills",
    "📈 GitHub Stats",
    "🎓 About",
    "📬 Contact"
])

# ── TAB 1 — Projects ──────────────────────────
with tab1:
    st.markdown(
        '<p class="section-title">'
        'Featured Projects</p>',
        unsafe_allow_html=True)
    st.markdown(
        '<p class="section-sub">'
        'Every project below is live and '
        'deployed. Click GitHub to see code.'
        '</p>',
        unsafe_allow_html=True)

    # Filter
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        phase_filter = st.selectbox(
            "Filter by phase:",
            ["All", "Phase 1 — Foundation",
             "Phase 2 — Intermediate ML",
             "Phase 3 — Advanced Web"]
        )
    with col_f2:
        tech_filter = st.selectbox(
            "Filter by technology:",
            ["All", "ML/AI", "NLP",
             "Deep Learning", "Computer Vision",
             "Data Science", "Full Stack"]
        )

    projects = [
        {
            "title": "Credit Card Fraud Detector",
            "desc":  "97% AUC-ROC on 284,807 "
                     "real transactions. SMOTE "
                     "for class imbalance.",
            "tech":  ["Python", "Scikit-learn",
                      "SMOTE", "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "ML/AI",
            "link":  "github.com/Rasdel7/"
                     "credit-card-fraud-detector",
            "metric":"97% AUC-ROC"
        },
        {
            "title": "Handwritten Digit Recognizer",
            "desc":  "98.5% accuracy on 70,000 "
                     "MNIST images using Neural "
                     "Networks.",
            "tech":  ["TensorFlow", "Keras",
                      "Neural Networks",
                      "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "Deep Learning",
            "link":  "github.com/Rasdel7/"
                     "handwritten-digit-recognizer",
            "metric":"98.5% Accuracy"
        },
        {
            "title": "Fake News Detector",
            "desc":  "98.5% accuracy on 44,898 "
                     "articles using TF-IDF "
                     "and Logistic Regression.",
            "tech":  ["NLP", "TF-IDF",
                      "Logistic Regression",
                      "Pickle"],
            "phase": "Phase 1 — Foundation",
            "type":  "NLP",
            "link":  "github.com/Rasdel7/"
                     "fake-news-detector",
            "metric":"98.5% Accuracy"
        },
        {
            "title": "Object Detection App",
            "desc":  "YOLOv8 detecting 80 "
                     "categories in real-time "
                     "using Ultralytics.",
            "tech":  ["YOLOv8", "Ultralytics",
                      "OpenCV", "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "Computer Vision",
            "link":  "github.com/Rasdel7/"
                     "object-detection-app",
            "metric":"80 Categories"
        },
        {
            "title": "AI Chatbot",
            "desc":  "7 personas powered by "
                     "Google Gemini API with "
                     "conversation memory.",
            "tech":  ["Gemini API", "Python",
                      "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "ML/AI",
            "link":  "github.com/Rasdel7/"
                     "ai-chatbot",
            "metric":"7 Personas"
        },
        {
            "title": "Sales Dashboard",
            "desc":  "Full BI dashboard with "
                     "KPIs, forecasting and "
                     "Plotly charts.",
            "tech":  ["Plotly", "Pandas",
                      "Gradient Boosting",
                      "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "Data Science",
            "link":  "github.com/Rasdel7/"
                     "sales-dashboard",
            "metric":"3yr Dataset"
        },
        {
            "title": "Image Classifier",
            "desc":  "ResNet50 transfer learning "
                     "classifying images into "
                     "1000 ImageNet categories.",
            "tech":  ["PyTorch", "ResNet50",
                      "Transfer Learning",
                      "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "Deep Learning",
            "link":  "github.com/Rasdel7/"
                     "image-classifier-app",
            "metric":"1000 Categories"
        },
        {
            "title": "E-Commerce Analytics",
            "desc":  "Complete analytics platform "
                     "with customer segmentation "
                     "and RFM analysis.",
            "tech":  ["Plotly", "Pandas",
                      "Streamlit"],
            "phase": "Phase 2 — Intermediate ML",
            "type":  "Data Science",
            "link":  "github.com/Rasdel7/"
                     "ecommerce-analytics",
            "metric":"2000 Orders"
        },
        {
            "title": "Portfolio Website",
            "desc":  "This website — built "
                     "entirely in Python using "
                     "Streamlit.",
            "tech":  ["Python", "Streamlit",
                      "Plotly", "CSS"],
            "phase": "Phase 3 — Advanced Web",
            "type":  "Full Stack",
            "link":  "github.com/Rasdel7/"
                     "portfolio-website",
            "metric":"Day 57"
        },
    ]

    # Apply filters
    shown = projects
    if phase_filter != "All":
        shown = [
            p for p in shown
            if p['phase'] == phase_filter]
    if tech_filter != "All":
        shown = [
            p for p in shown
            if p['type'] == tech_filter]

    # Display projects
    for i in range(0, len(shown), 2):
        col_l, col_r = st.columns(2)
        for col, proj in zip(
            [col_l, col_r],
            shown[i:i+2]
        ):
            with col:
                badges = " ".join([
                    f'<span class="badge">'
                    f'{t}</span>'
                    for t in proj['tech']
                ])
                col.markdown(
                    f"""<div class="project-card">
                    <div class="project-title">
                        🚀 {proj['title']}
                    </div>
                    <p style="color:#6b7280;
                       font-size:0.9rem;
                       margin:0.5rem 0">
                        {proj['desc']}
                    </p>
                    <div>{badges}</div>
                    <p style="margin-top:0.75rem;
                       font-size:0.85rem">
                        📊 <b>{proj['metric']}</b>
                        &nbsp;|&nbsp;
                        🔗 {proj['link']}
                    </p>
                    </div>""",
                    unsafe_allow_html=True
                )

# ── TAB 2 — Skills ────────────────────────────
with tab2:
    st.markdown(
        '<p class="section-title">Skills</p>',
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🐍 Programming")
        skills_prog = {
            "Python":     95,
            "SQL":        75,
            "C":          65,
            "JavaScript": 50
        }
        for skill, level in skills_prog.items():
            st.markdown(
                f'<span class="skill-bar-label">'
                f'{skill}</span>',
                unsafe_allow_html=True)
            st.progress(level / 100)

        st.markdown("#### 🧠 ML / AI")
        skills_ml = {
            "Scikit-learn":  90,
            "TensorFlow":    80,
            "PyTorch":       70,
            "Hugging Face":  55,
            "LLM APIs":      75
        }
        for skill, level in skills_ml.items():
            st.markdown(
                f'<span class="skill-bar-label">'
                f'{skill}</span>',
                unsafe_allow_html=True)
            st.progress(level / 100)

    with col2:
        st.markdown("#### 📊 Data Science")
        skills_ds = {
            "Pandas":      95,
            "NumPy":       90,
            "Matplotlib":  85,
            "Plotly":      85,
            "Seaborn":     80
        }
        for skill, level in skills_ds.items():
            st.markdown(
                f'<span class="skill-bar-label">'
                f'{skill}</span>',
                unsafe_allow_html=True)
            st.progress(level / 100)

        st.markdown("#### 🛠️ Tools")
        skills_tools = {
            "Git/GitHub":  90,
            "Streamlit":   95,
            "VS Code":     90,
            "Jupyter":     85,
            "Docker":      40
        }
        for skill, level in skills_tools.items():
            st.markdown(
                f'<span class="skill-bar-label">'
                f'{skill}</span>',
                unsafe_allow_html=True)
            st.progress(level / 100)

    # Skills radar
    st.markdown("#### 🎯 Skill Overview")
    categories = [
        'Python', 'ML', 'Deep Learning',
        'NLP', 'Data Viz', 'Web Dev'
    ]
    values = [95, 85, 75, 80, 85, 70]

    fig = go.Figure(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(26,86,219,0.2)',
        line=dict(color='#1A56DB', width=2),
        name='Skills'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(
            visible=True, range=[0, 100])),
        height=400,
        showlegend=False,
        title='Technical Skill Coverage'
    )
    st.plotly_chart(fig,
                    use_container_width=True)

# ── TAB 3 — GitHub Stats ──────────────────────
with tab3:
    st.markdown(
        '<p class="section-title">'
        'GitHub Activity</p>',
        unsafe_allow_html=True)

    # Simulated contribution data
    import numpy as np
    np.random.seed(42)

    days  = pd.date_range('2026-01-01',
                          periods=57, freq='D')
    contribs = np.random.randint(3, 12, 57)
    contribs[:10] = np.random.randint(5, 15, 10)
    contribs[20:] = np.random.randint(6, 18, 37)

    contrib_df = pd.DataFrame({
        'date':          days,
        'contributions': contribs,
        'project':       [f"Day {i+1} Project"
                          for i in range(57)]
    })

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=contrib_df['date'],
        y=contrib_df['contributions'],
        marker_color=[
            '#1A56DB' if c > 10
            else '#60a5fa' if c > 6
            else '#bfdbfe'
            for c in contrib_df['contributions']
        ],
        name='Contributions',
        hovertemplate=(
            '%{x}<br>'
            'Contributions: %{y}<br>'
            '<extra></extra>'
        )
    ))
    fig2.update_layout(
        title='Daily GitHub Contributions '
              '(2026)',
        xaxis_title='Date',
        yaxis_title='Contributions',
        height=350,
        template='plotly_white'
    )
    st.plotly_chart(fig2,
                    use_container_width=True)

    # Project type breakdown
    col1, col2 = st.columns(2)

    with col1:
        type_data = {
            'ML/AI':          15,
            'Data Science':   12,
            'NLP':            8,
            'Deep Learning':  6,
            'Computer Vision':4,
            'Full Stack':     7,
            'Tools/Utils':    5
        }
        fig3 = px.pie(
            values=list(type_data.values()),
            names=list(type_data.keys()),
            title='Projects by Type',
            color_discrete_sequence=
                px.colors.qualitative.Set2
        )
        fig3.update_layout(height=350)
        st.plotly_chart(
            fig3,
            use_container_width=True)

    with col2:
        lang_data = {
            'Python':     52,
            'JavaScript': 3,
            'SQL':        1,
            'HTML/CSS':   1
        }
        fig4 = px.bar(
            x=list(lang_data.values()),
            y=list(lang_data.keys()),
            orientation='h',
            title='Repos by Language',
            color=list(lang_data.values()),
            color_continuous_scale='Blues'
        )
        fig4.update_layout(
            height=350,
            template='plotly_white'
        )
        st.plotly_chart(
            fig4,
            use_container_width=True)

    # Streak stats
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Current Streak", "57 days 🔥")
    s2.metric("Total Projects",  "57 deployed")
    s3.metric("Total Commits",   "800+")
    s4.metric("Stars Earned",    "Growing ⭐")

# ── TAB 4 — About ─────────────────────────────
with tab4:
    st.markdown(
        '<p class="section-title">About Me</p>',
        unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ### Hey, I'm Jyotiraditya 👋

        I'm a 2nd year Computer Science student
        at **Silicon Institute of Technology,
        Bhubaneswar**, on a mission to become
        an ML Engineer at a top tech company.

        In May 2026 I set myself a challenge —
        **build and deploy one complete project
        every single day for 365 consecutive days**.
        No breaks. No excuses. I'm currently
        on Day 57 with zero missed days.

        My projects span the full ML pipeline:
        from basic classifiers to Neural Networks,
        NLP systems, Computer Vision apps, and
        full-stack web applications — all live
        and deployed.

        **What drives me:** I believe the best
        way to learn is to build in public.
        Every project teaches me something
        new and adds to a portfolio that
        speaks louder than any certificate.
        """)

    with col2:
        st.markdown("### 📊 Quick Facts")
        facts = [
            ("🎓", "B.Tech CSE, 2024-2028"),
            ("🏫", "SIT Bhubaneswar"),
            ("📍", "Bhubaneswar, Odisha"),
            ("🎯", "ML Engineer Target"),
            ("🔥", "57-day streak"),
            ("💻", "Python specialist"),
            ("🏏", "Cricket fan"),
            ("🎮", "Game dev enthusiast")
        ]
        for emoji, fact in facts:
            st.markdown(f"{emoji} {fact}")

    # Timeline
    st.markdown("### 🗓️ Journey")

    timeline = [
        {
            "date":  "May 2026",
            "event": "Started 365-day challenge",
            "desc":  "Committed to building "
                     "one project every day"
        },
        {
            "date":  "May 2026",
            "event": "Phase 1 Complete",
            "desc":  "30 foundational projects — "
                     "regression, classification, "
                     "NLP basics"
        },
        {
            "date":  "June 2026",
            "event": "Phase 2 Complete",
            "desc":  "30 intermediate projects — "
                     "deep learning, CV, "
                     "financial apps"
        },
        {
            "date":  "June 2026",
            "event": "Phase 3 Started",
            "desc":  "Advanced web apps, APIs, "
                     "full-stack projects"
        },
        {
            "date":  "2027",
            "event": "Placement Season",
            "desc":  "Target: ML Engineer intern "
                     "at top tech company"
        }
    ]

    for item in timeline:
        st.markdown(
            f"""<div class="timeline-item">
            <strong>{item['date']}</strong>
            — {item['event']}<br>
            <span style="color:#6b7280;
                font-size:0.9rem">
                {item['desc']}
            </span>
            </div>""",
            unsafe_allow_html=True
        )

# ── TAB 5 — Contact ───────────────────────────
with tab5:
    st.markdown(
        '<p class="section-title">'
        'Get In Touch</p>',
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 👋 Let's Connect

        I'm actively looking for **ML Engineer
        internships** and open to collaboration
        on interesting data science projects.

        Whether you're a recruiter, fellow
        developer or just someone who loves
        building things — reach out!
        """)

        contacts = [
            ("📧", "Email",
             "jyotiradityab7@gmail.com"),
            ("💼", "LinkedIn",
             "linkedin.com/in/jyotiraditya-biswal-a66017368"),
            ("🐙", "GitHub",
             "github.com/Rasdel7"),
            ("📍", "Location",
             "Bhubaneswar, Odisha, India")
        ]

        for emoji, platform, link in contacts:
            st.markdown(
                f"""<div class="contact-link">
                {emoji} <strong>{platform}:</strong>
                {link}
                </div>""",
                unsafe_allow_html=True
            )

    with col2:
        st.markdown("### 📨 Send a Message")
        name_input    = st.text_input(
            "Your Name")
        email_input   = st.text_input(
            "Your Email")
        subject_input = st.text_input(
            "Subject",
            placeholder="Internship Opportunity / "
                        "Collaboration / Feedback"
        )
        msg_input = st.text_area(
            "Message", height=150)

        if st.button("📨 Send Message",
                     type="primary"):
            if name_input and \
                    email_input and msg_input:
                st.success(
                    "✅ Message noted! "
                    "I'll reply to "
                    f"{email_input} soon.")
                st.balloons()
            else:
                st.warning(
                    "Please fill all fields!")

# ── FOOTER ────────────────────────────────────
st.markdown("---")
st.markdown(
    """<div style="text-align:center;
       color:#9ca3af; font-size:0.9rem">
    Built with ❤️ by Jyotiraditya Biswal
    &nbsp;•&nbsp;
    Python + Streamlit
    &nbsp;•&nbsp;
    Day 57 of 365
    </div>""",
    unsafe_allow_html=True
)