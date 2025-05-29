import streamlit as st
import torch 
import torch.nn as nn 
import torch.nn.functional as F
import matplotlib.pyplot as plt
import pymongo
from pymongo import MongoClient
import certifi
import numpy as np
import os


os.environ['KMP_DUPLICATE_LIB_OK']='True'

ca = certifi.where()

cluster = MongoClient("mongodb+srv://narashimantarun:nnohdI3YFye8pqsL@cluster0.k1tq2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",tlsCAFile=ca)
db = cluster['test']
collection = db['test']

SavingsCollection = db['SavingsCollection']
SpendingsCollection = db['Spendings']

usr = st.session_state['user']
lg = st.session_state['logged_in']


def main():
    print(usr)
    user_data = SavingsCollection.find_one({"UserName": usr})

    if(user_data is not None):
        userspendl = SpendingsCollection.find_one({"Username": usr})

        if(userspendl is not None):
            spent_Potential_Savings_Groceries = userspendl['Potential_Savings_Groceries']
            spent_Potential_Savings_Transport = userspendl['Potential_Savings_Transport']
            spent_Potential_Savings_Eating_Out = userspendl['Potential_Savings_Eating_Out']
            spent_Potential_Savings_Entertainment = userspendl['Potential_Savings_Entertainment']
            spent_Potential_Savings_Utilities = userspendl['Potential_Savings_Utilities']
            spent_Potential_Savings_Healthcare = userspendl['Potential_Savings_Healthcare']
            spent_Potential_Savings_Education = userspendl['Potential_Savings_Education']
            spent_Potential_Savings_Miscellaneous = userspendl['Potential_Savings_Miscellaneous']

            #WEBSITE IS HERE
            st.title("Spending Tracker")

            spendLimits = user_data["SpendLimits"]



            GroceryIntake = st.number_input("Enter money spent on grocery")
            TransportIntake = st.number_input("Enter money spent on transport")
            EatingOutIntake = st.number_input("Enter money spent on eating out")
            EntertainmentIntake = st.number_input("Enter money spent on entertainment")
            UtilitiesIntake = st.number_input("Enter money spent on utilities")
            HealthcareIntake = st.number_input("Enter money spent on healthcare")
            EducationIntake = st.number_input("Enter money spent on education")
            MiscellaneousIntake = st.number_input("Enter money spent on miscellaneous")

            st.subheader("Groceries : {}/{}".format(int(spent_Potential_Savings_Groceries), int(spendLimits[0])))
            GroceryBar = st.progress(spent_Potential_Savings_Groceries / spendLimits[0])
            st.subheader("Transport : {}/{}".format(int(spent_Potential_Savings_Transport), int(spendLimits[1])))
            TransportBar = st.progress(spent_Potential_Savings_Transport / spendLimits[1])
            st.subheader("Eating Out : {}/{}".format(int(spent_Potential_Savings_Eating_Out), int(spendLimits[2])))
            EatingOutBar = st.progress(spent_Potential_Savings_Eating_Out / spendLimits[2])
            st.subheader("Entertainment : {}/{}".format(int(spent_Potential_Savings_Entertainment), int(spendLimits[3])))
            EntertainmentBar = st.progress(spent_Potential_Savings_Entertainment / spendLimits[3])
            st.subheader("Utilities : {}/{}".format(int(spent_Potential_Savings_Utilities), int(spendLimits[4])))
            UtilitiesBar = st.progress(spent_Potential_Savings_Utilities / spendLimits[4])
            st.subheader("Healthcare : {}/{}".format(int(spent_Potential_Savings_Healthcare), int(spendLimits[5])))
            HealthcareBar = st.progress(spent_Potential_Savings_Healthcare / spendLimits[5])
            st.subheader("Education : {}/{}".format(int(spent_Potential_Savings_Education), int(spendLimits[6])))
            EducationBar = st.progress(spent_Potential_Savings_Education / spendLimits[6])
            st.subheader("Miscellaneous : {}/{}".format(int(spent_Potential_Savings_Miscellaneous), int(spendLimits[7])))
            MiscellaneousBar = st.progress(spent_Potential_Savings_Miscellaneous / spendLimits[7])

            b = st.button("Update")

            if(b):
                temp_grocery = (spent_Potential_Savings_Groceries + GroceryIntake) / spendLimits[0]
                temp_transport = (spent_Potential_Savings_Transport + TransportIntake) / spendLimits[1]
                temp_eating_out = (spent_Potential_Savings_Eating_Out + EatingOutIntake) / spendLimits[2]
                temp_entertainment = (spent_Potential_Savings_Entertainment + EntertainmentIntake) / spendLimits[3]
                temp_utilities = (spent_Potential_Savings_Utilities + UtilitiesIntake) / spendLimits[4]
                temp_healthcare = (spent_Potential_Savings_Healthcare + HealthcareIntake) / spendLimits[5]
                temp_education = (spent_Potential_Savings_Education + EducationIntake) / spendLimits[6]
                temp_miscellaneous = (spent_Potential_Savings_Miscellaneous + MiscellaneousIntake) / spendLimits[7]


                update_grocery = spent_Potential_Savings_Groceries + GroceryIntake
                update_transport = spent_Potential_Savings_Transport + TransportIntake
                update_eating_out = spent_Potential_Savings_Eating_Out + EatingOutIntake
                update_entertainment = spent_Potential_Savings_Entertainment + EntertainmentIntake
                update_utilities = spent_Potential_Savings_Utilities + UtilitiesIntake
                update_healthcare = spent_Potential_Savings_Healthcare + HealthcareIntake
                update_education = spent_Potential_Savings_Education + EducationIntake
                update_miscellaneous = spent_Potential_Savings_Miscellaneous + MiscellaneousIntake

                if temp_grocery >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Groceries")
                    temp_grocery = 0
                    update_grocery = 0

                if temp_transport >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Transport")
                    temp_transport = 0
                    update_transport = 0

                if temp_eating_out >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Eating Out")
                    temp_eating_out = 0
                    update_eating_out = 0

                if temp_entertainment >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Entertainment")
                    temp_entertainment = 0
                    update_entertainment = 0

                if temp_utilities >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Utilities")
                    temp_utilities = 0
                    update_utilities = 0

                if temp_healthcare >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Healthcare")
                    temp_healthcare = 0
                    update_healthcare = 0

                if temp_education >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Education")
                    temp_education = 0
                    update_education = 0

                if temp_miscellaneous >= 1.0:
                    st.balloons()
                    st.toast("You have completed your monthly allowance for Miscellaneous")
                    temp_miscellaneous = 0
                    update_miscellaneous = 0

                user_savings_data = {
                    "Potential_Savings_Groceries": update_grocery,
                    "Potential_Savings_Transport": update_transport,
                    "Potential_Savings_Eating_Out": update_eating_out,
                    "Potential_Savings_Entertainment": update_entertainment,
                    "Potential_Savings_Utilities": update_utilities,
                    "Potential_Savings_Healthcare": update_healthcare,
                    "Potential_Savings_Education": update_education,
                    "Potential_Savings_Miscellaneous": update_miscellaneous
                    }
                
                SpendingsCollection.update_one({"Username" : usr},{"$set" : user_savings_data})
                st.success("Updated Successfully")

                GroceryBar.progress(temp_grocery, "Grocery expenditures")
                TransportBar.progress(temp_transport, "Transport expenditures")
                EatingOutBar.progress(temp_eating_out, "Eating Out expenditures")
                EntertainmentBar.progress(temp_entertainment, "Entertainment expenditures")
                UtilitiesBar.progress(temp_utilities, "Utilities expenditures")
                HealthcareBar.progress(temp_healthcare, "Healthcare expenditures")
                EducationBar.progress(temp_education, "Education expenditures")
                MiscellaneousBar.progress(temp_miscellaneous, "Miscellaneous expenditures")



            


        else:
            user_savings_data = {
                "Username" : usr,
            "Potential_Savings_Groceries": 0,
            "Potential_Savings_Transport": 0,
            "Potential_Savings_Eating_Out": 0,
            "Potential_Savings_Entertainment": 0,
            "Potential_Savings_Utilities": 0,
            "Potential_Savings_Healthcare": 0,
            "Potential_Savings_Education": 0,
            "Potential_Savings_Miscellaneous": 0
            }

            SpendingsCollection.insert_one(user_savings_data)

            print("reload")



                  


    else:
        st.error("Please open up modelpage")



if __name__ == '__main__':
    if(lg == False):
        st.error('please login to access this page')
    else:
        main()


