import streamlit as st
import joblib
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Loan Approval Prediction System",
    page_icon="🏦",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================
model = joblib.load("Loan_Approval_Prediction_System.joblib")

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

/* ==========================
   BACKGROUND
========================== */

.stApp{
background-image:url("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1800&q=80");
background-size:cover;
background-position:center;
background-repeat:no-repeat;
}

/* ==========================
   MAIN CONTAINER
========================== */

.main-box{
background:rgba(20,35,60,0.55);
padding:30px;
border-radius:20px;
backdrop-filter:blur(12px);
box-shadow:0px 8px 20px rgba(0,0,0,0.5);
}

/* ==========================
   TITLE
========================== */

.title{
text-align:center;
font-size:50px;
font-weight:900;
color:white;
text-shadow:3px 3px 8px rgba(0,0,0,0.8);
}

.subtitle{
text-align:center;
font-size:20px;
font-weight:bold;
color:#E0FFFF;
margin-bottom:25px;
text-shadow:2px 2px 5px rgba(0,0,0,0.8);
}

/* ==========================
   INPUT LABELS
========================== */

.stNumberInput label,
.stSelectbox label,
.stSlider label{

font-size:20px !important;
font-weight:800 !important;
color:#FFD700 !important;
text-shadow:2px 2px 6px rgba(0,0,0,1);

}

/* ==========================
   INPUT BOXES
========================== */

.stNumberInput input{

font-size:18px !important;
font-weight:bold !important;
color:black !important;

}

/* ==========================
   SELECT BOX
========================== */

.stSelectbox div[data-baseweb="select"]{

font-size:18px !important;
font-weight:bold !important;
color:black !important;

}

/* ==========================
   SLIDER VALUE
========================== */

.stSlider span{

font-size:18px !important;
font-weight:bold !important;

}

/* ==========================
   BUTTON
========================== */

.stButton>button{

width:100%;
height:60px;
font-size:22px;
font-weight:bold;
border-radius:12px;
background:linear-gradient(90deg,#0d6efd,#00b4d8);
color:white;
border:none;
transition:0.3s;

}

.stButton>button:hover{

background:linear-gradient(90deg,#198754,#20c997);
transform:scale(1.03);

}

/* ==========================
   RESULT
========================== */

.result{

background:white;
padding:20px;
border-radius:15px;
font-size:70px;
text-align:center;
font-weight:bold;

}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.markdown("<div class='title'>🏦 Loan Approval Prediction System</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>AI Powered Smart Loan Approval Predictor</div>", unsafe_allow_html=True)

st.markdown("<div class='main-box'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# =====================================
# COLUMN 1
# =====================================

with col1:

    Applicant_Income = st.number_input("Applicant Income", 0)

    Coapplicant_Income = st.number_input("Coapplicant Income", 0)

    Employment_Status = st.selectbox(
        "Employment Status",
        ["Salaried","Self-employed","Contract","Unemployed"]
    )

    Age = st.number_input("Age",18,80)

    Marital_Status = st.selectbox(
        "Marital Status",
        ["Single","Married"]
    )

    Dependents = st.selectbox(
        "Dependents",
        [0,1,2,3]
    )

# =====================================
# COLUMN 2
# =====================================

with col2:

    Credit_Score = st.slider(
        "Credit Score",
        300,
        900,
        650
    )

    Existing_Loans = st.number_input(
        "Existing Loans",
        0
    )

    DTI_Ratio = st.slider(
        "DTI Ratio",
        0.0,
        1.0,
        0.30
    )

    Savings = st.number_input(
        "Savings",
        0
    )

    Collateral_Value = st.number_input(
        "Collateral Value",
        0
    )

    Loan_Amount = st.number_input(
        "Loan Amount",
        0
    )

# =====================================
# COLUMN 3
# =====================================

with col3:

    Loan_Term = st.number_input(
        "Loan Term (Months)",
        1
    )

    Loan_Purpose = st.selectbox(
         "Loan Purpose",
        ["Personal","Car","Business","Home","Education"]
    )

    Property_Area = st.selectbox(
        "Property Area",
        ["Urban","Semiurban","Rural"]
    )

    Education_Level = st.selectbox(
        "Education Level",
        ["Graduate","Not Graduate"]
    )

    Gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    Employer_Category = st.selectbox(
        "Employer Category",
        ["Private","Government","Unemployed","MNC","Business"]
    )

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# PREDICTION
# =====================================

if st.button("🔍 Predict Loan Approval", use_container_width=True):

    data = pd.DataFrame({

        "Applicant_Income":[Applicant_Income],
        "Coapplicant_Income":[Coapplicant_Income],
        "Employment_Status":[Employment_Status],
        "Age":[Age],
        "Marital_Status":[Marital_Status],
        "Dependents":[Dependents],
        "Credit_Score":[Credit_Score],
        "Existing_Loans":[Existing_Loans],
        "DTI_Ratio":[DTI_Ratio],
        "Savings":[Savings],
        "Collateral_Value":[Collateral_Value],
        "Loan_Amount":[Loan_Amount],
        "Loan_Term":[Loan_Term],
        "Loan_Purpose":[Loan_Purpose],
        "Property_Area":[Property_Area],
        "Education_Level":[Education_Level],
        "Gender":[Gender],
        "Employer_Category":[Employer_Category]

    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        

        st.success("✅ Loan Approved")
        st.balloons()

    else:

        st.error("❌ Loan Rejected")