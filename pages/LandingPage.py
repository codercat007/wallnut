import streamlit as st
import os
import pymongo
from pymongo import MongoClient
import certifi

 
ca = certifi.where()

cluster = MongoClient("mongodb+srv://narashimantarun:nnohdI3YFye8pqsL@cluster0.k1tq2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",tlsCAFile=ca)
db = cluster['test']
collection = db['test']

usr = st.session_state['user']
lg = st.session_state['logged_in']





def main():
    
    unames = collection.find_one({"UserName":usr})
    
    st.title("welcome to Wallnut, {}".format(usr))


    if unames is None:

        with st.form("IntroForm"):
            st.write("Please fill out the following information:")
            income = st.number_input("Enter Income")
            age = st.number_input("Enter Age")
            dependents = st.number_input("Enter number of dependents")
            occupation = st.text_input("Enter Occupation")
            rent = st.number_input("Enter Rent")
            loan_repayment = st.number_input("Enter Loan Repayment")
            insurance = st.number_input("Enter Insurance")
            groceries = st.number_input("Enter Groceries")
            transport = st.number_input("Enter Transport")
            eating_out = st.number_input("Enter Eating Out")
            entertainment = st.number_input("Enter Entertainment")
            utilities = st.number_input("Enter Utilities")
            healthcare = st.number_input("Enter Healthcare")
            education = st.number_input("Enter Education")
            miscellaneous = st.number_input("Enter Miscellaneous")
            desired_savings_percentage = st.number_input("Enter Desired Savings Percentage")
            desired_savings = st.number_input("Enter Desired Savings")


            if st.form_submit_button("Submit"):
                
                post = {
                    "UserName" : usr,
                    "Income": income,
                    "Age": age,
                    "Dependents": dependents,
                    "Occupation": occupation,
                    "Rent": rent,
                    "Loan_Repayment": loan_repayment,
                    "Insurance": insurance,
                    "Groceries": groceries,
                    "Transport": transport,
                    "Eating_Out": eating_out,
                    "Entertainment": entertainment,
                    "Utilities": utilities,
                    "Healthcare": healthcare,
                    "Education": education,
                    "Miscellaneous": miscellaneous,
                    "Desired_Savings_Percentage": desired_savings_percentage,
                    "Desired_Savings": desired_savings
                 }
                collection.insert_one(post)
                st.success("Form Submitted")
        

    else:
        st.success("Thank you for filling out the form, you may proceed to your plan")



if __name__ == '__main__':
    if(lg == False):
        st.error('please login to access this page')
    else:
        main()
