import pickle
import streamlit as st

model=pickle.load(open('new_model.pkl','rb'))
def prediction(Number_of_Open_Accounts,Years_of_Credit_History,Maximum_Open_Credit,Current_Loan_Amount,Current_Credit_Balance,Monthly_Debt,Annual_Income,Months_since_last_delinquent,Home_Ownership,Term,Years_in_current_job):
   
    prediction = model.predict([[Number_of_Open_Accounts,Years_of_Credit_History,Maximum_Open_Credit,Current_Loan_Amount,Current_Credit_Balance,Monthly_Debt,Annual_Income,Months_since_last_delinquent,Home_Ownership,Term,Years_in_current_job]])
    proba = model.predict_proba([[Number_of_Open_Accounts,Years_of_Credit_History,Maximum_Open_Credit,Current_Loan_Amount,Current_Credit_Balance,Monthly_Debt,Annual_Income,Months_since_last_delinquent,Home_Ownership,Term,Years_in_current_job]])
    if predicted==1:
        print("USER IS A DEFAULTER\n\nTHE PROBABILITY OF DEFAULT is")
        return round(proba[0][1],2)
    else:
        print("USER IS NOT A DEFAULTER\n\nTHE PROBABILITY OF DEFAULT is")
        return round(proba[0][1],2)
    
def main():
    st.title("LOAN DEFAULT PREDICTION")
    html_temp = """
    <div style = "background-color:#025246; padding:10px">
    <h2 style = "color:white;text-align:center;">PREDICT WHEATHER THE INDIVIDUAL WILL DEFAULT OR NOT</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Number_of_Open_Accounts = st.slider("NO. OF OPEN ACCOUNTS", 0, 50)
       
    Years_of_Credit_History = st.number_input("YEARS OF CREDIT HISTORY", 0.0)
    
    Maximum_Open_Credit = st.number_input("MAXIMUM OPEN CREDIT", 0)
    
    Current_Loan_Amount = st.number_input("CURRENT LOAN AMOUNT", 0)
    
    Current_Credit_Balance = st.number_input("CURRENT CREDIT BALANCE", 0)
    
    Monthly_Debt = st.number_input("MONTHLY DEBT", 0)
    
    Annual_Income = st.number_input("ANNUAL INCOME", 0)
    
    Months_since_last_delinquent = st.slider("MONTHS SINCE LAST DELINQUENT", 0, 120)
   
    Home_Ownership = st.selectbox("HOME OWNERSHIP (select -0.19 for HAVE and HOME MORTGAGE, select 0.09 for OWN HOME and select 0.18 for RENT)", [-0.19,0.09,0.18])
        
    Term = st.selectbox("TERM (For SHORT TERM select -0.24 and LONG TERM select 0.58)", [-.24,0.58])
 
    Years_in_current_job = st.selectbox("YEARS IN CURRENT JOB (For 1 YEAR, < 1 YEAR and 10+ YEARS select 0.13, For 4 YEARS, 7 YEARS, 6 YEARS and 2 YEARS select 0.01, For 9 YEARS, 5 YEARS and 3 YEARS select -0.68 and For 8 YEARS select -0.11)", [0.13,0.01,-0.68,-0.11])

    more_html='''
    <div style = "background-color:#F08080; padding:10px">
    <h2 style = "color:white;text-align:center;"> THE INDIVIDUAL IS A DEFAULTER </h2>
    </div>
    '''
    
    less_html='''
    <div style = "background-color: #056608; padding:10px">
    <h2 style = "color:white;text-align:center;"> THE INDIVIDUAL IS NOT A DEFAULTER </h2>
    </div>
    '''
    
    if st.button("SUBMIT"):
        output = prediction(Number_of_Open_Accounts,Years_of_Credit_History,Maximum_Open_Credit,Current_Loan_Amount,Current_Credit_Balance,Monthly_Debt,Annual_Income,Months_since_last_delinquent,Home_Ownership,Term,Years_in_current_job)
        if(output>=0.5):
            st.markdown(more_html, unsafe_allow_html=True)
        else:
            st.markdown(less_html, unsafe_allow_html=True)
        st.metric(label='PROBABILITY OF DEFAULT is', value = str(output))

if __name__=='__main__':
    main()
