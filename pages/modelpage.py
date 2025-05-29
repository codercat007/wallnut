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


usr = st.session_state['user']
lg = st.session_state['logged_in']

def fetch_user_data(username):
    user_data = collection.find_one({"UserName": username})
    
    if user_data:
        keys_order = ['Income', 'Age', 'Dependents', 'Rent',
                      'Loan_Repayment', 'Insurance', 'Groceries', 'Transport', 'Eating_Out',
                      'Entertainment', 'Utilities', 'Healthcare', 'Education',
                      'Miscellaneous', 'Desired_Savings_Percentage', 'Desired_Savings',
                      'Disposable_Income']
        numeric_values = [user_data.get(key, 0) for key in keys_order]
        
        return np.array(numeric_values, dtype=np.float32)
    else:
        print("User not found")
        return None
    
class ClassicalANN(nn.Module):

    def __init__(self,in_features=5):
        super().__init__()
        self.fc1 = nn.Linear(17,64)
        self.fc2 = nn.Linear(64,32)
        self.fc7 = nn.Linear(32,8)

    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc7(x)

        return x

def load_model(model_path):
    model = torch.load(model_path)
    return model

def get_prediction(model_path, inputs):
    m = ClassicalANN()
    m.load_state_dict(torch.load(model_path))
    with torch.no_grad():
        inputs = torch.tensor(inputs, dtype=torch.float32)
        outputs = m(inputs)
    return outputs

def plot_pie_chart(outputs):
    labels = ['Potential_Savings_Groceries',
       'Potential_Savings_Transport', 'Potential_Savings_Eating_Out',
       'Potential_Savings_Entertainment', 'Potential_Savings_Utilities',
       'Potential_Savings_Healthcare', 'Potential_Savings_Education',
       'Potential_Savings_Miscellaneous']
    plt.figure(figsize=(6, 6))
    plt.pie(outputs, labels=labels, startangle=140,autopct=lambda p: '{:.0f}'.format(p * sum(outputs) / 100))
    plt.axis('equal')
    st.pyplot(plt)

def MakeSlideBars(ahh):
    pass    

def main():
    unames = collection.find_one({"UserName":usr})
    st.title("welcome to Wallnut, {}".format(usr))
    if unames is None:
        st.error("Please fill the form to access this page")
    
    else:
        IsUnameInModel = SavingsCollection.find_one({"UserName":usr})
        if(IsUnameInModel is None):

            model_path = "model.pth"
            user_data_array = fetch_user_data(usr)  
            preds = get_prediction(model_path, user_data_array)
            preds = preds.numpy()
            ahh = []
            for x in preds:
                if(x<0):
                    
                    ahh.append(int(-1 * x))
                else:
                    ahh.append(int(x))

            #ahh = np.array(ahh)
            #st.write(ahh)
            post = {
                "UserName" : usr,
                "SpendLimits" : list(ahh)
            }

            SavingsCollection.insert_one(post)
            st.success("Refresh page to access features")
        else:
            ahh = IsUnameInModel["SpendLimits"]
            plot_pie_chart(ahh)





if __name__ == '__main__':
    if(lg == False):
        st.error('please login to access this page')
    else:
        main()
