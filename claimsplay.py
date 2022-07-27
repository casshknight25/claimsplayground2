import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title("Claims Data Explorer")

notification = 'claims.csv'
motor = 'PICHclaims.csv'
notdata = pd.read_csv(notification)
motdata = pd.read_csv(motor)

data = st.selectbox("Select Data Set", ("Notification Data by LOB", "Motor Claims",))
if data =='Notification Data by LOB':
    st.info("A report request has come in for a report explaining the different ways claims can be notified across the different lines of business. ")
    st.write(notdata)
    if st.checkbox("Data Summaries"):
        option = st.selectbox("Select a Column to Summarise", ("Line of Business", "Notification Type", "Claim Status"))
        if option == "Line of Business":
            st.write(notdata["Line of Business"].value_counts())
        if option == "Notification Type":
            st.write(notdata["Notification Type"].value_counts())
        if option == "Claim Status":
            st.write(notdata["Claim Status"].value_counts())
    if st.button("Summary Statistics"):
        st.write(notdata.describe().T)
        st.info("What do you notice about the difference in the total count of claims references compared to the unique count of claims references? What do you think this could mean?")

if data =='Motor Claims':
    st.info("A  request has come in for a report summarising motor claims received with PI and credit hire split by blame code")
    st.write(motdata)
    if st.checkbox("Data Summaries"):
        option = st.selectbox("Select a Column to Summarise", ("Blame Code", "Vehicle Make", "PI Indicator", "CH Indicator", "Latest Record"))
        if option == "Blame Code":
            st.write(motdata["Blame Code"].value_counts())
        if option == "Vehicle Make":
            st.write(motdata["Vehicle Make "].value_counts())
        if option == "PI Indicator":
            st.write(motdata["PI Indicator"].value_counts())
        if option == "CH Indicator":
                st.write(motdata["CH Indicator"].value_counts())
        if option == "Latest Record":
                    st.write(motdata["Latest Record "].value_counts())
    if st.button("Summary Statistics"):
        st.write(motdata.describe().T)


if data =='Notification Data by LOB':
    st.header("Exploratory Data Analysis")
    all_columns_names = notdata.columns.tolist()
    plots = st.selectbox("Select Type of Plot",("Bar","Line","Box","Pie"))
    select_column_X = st.selectbox("Select Columns To Plot", all_columns_names)
    if plots =="Bar" and select_column_X =="Line of Business" and st.button("Generate Plot"):
        lob_bar_chart = alt.Chart(notdata).mark_bar().encode(alt.X("Line of Business"), y="count()")
        st.altair_chart(lob_bar_chart, use_container_width=True)

    elif plots =="Bar" and select_column_X =="Notification Type" and st.button("Generate Plot"):
        not_bar_chart = alt.Chart(notdata).mark_bar().encode(alt.X("Notification Type"),y="count()")
        st.altair_chart(not_bar_chart, use_container_width=True)

    elif plots == "Pie" and select_column_X == "Line of Business" and st.button("Generate Plot"):
        labels = ["Motor", "Casualty", "PI", "Property"]
        values = [22,16,15,9]
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%',startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    elif plots == "Pie" and select_column_X == "Notification Type" and st.button("Generate Plot"):
        labels = ["Email", "Telephone", "Post", "MOJ","OIC"]
        values = [18,17,12,9,6]
        fig2, ax2 = plt.subplots()
        ax2.pie(values, labels=labels, autopct='%1.1f%%',startangle=90)
        ax2.axis('equal')
        st.pyplot(fig2)
        




