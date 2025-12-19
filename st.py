import streamlit as st
import pandas as pd

st.title("Market A/B Testing Analysis")

st.header("Overview")
st.write("""This project evaluates the effectiveness of a marketing ad campaign using A/B testing methodology. By comparing a test group (users exposed to ads) with a control group (users exposed to Public Service Announcements, PSAs), we assess whether ad exposure leads to a statistically significant improvement in user conversions

WORKFLOW:
1. Data Preparation
- Imported and inspected the dataset for structure, missing values and duplicate values.
- Applied outlier detection on the Total Ads and Most Ads Hour columns using the Interquartile Range (IQR) method to remove extreme values that could bias results.
2. Exploratory Data Analysis (EDA)
- Visualized conversion across Test (Ad) and Control (PSA) groups.
- Examined the distribution of Total Ads viewed and Most Ads Hours.
- Analyzed conversion patterns and identified peak ad exposure times by day and hour.
3. A/B Testing
- Split the dataset into Group A (Ad) and Group B (PSA).
- Calculated conversion rates for both groups.
- Conducted an Independent T-test to evaluate statistical significance of observed differences.

HYPOTHESIS
- Null Hypothesis (H₀): No difference exists in conversion rates between the Ad group and the PSA group.
- Alternative Hypothesis (H₁): Conversion rates differ between the Ad group and the PSA group (with the expectation that ads increase conversions).""")

st.header("Key Findings")

data = pd.read_csv("./dataset/marketing_AB.csv")
st.dataframe(data)
st.write(data.describe().round(2))

