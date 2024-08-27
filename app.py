import streamlit as st
import pickle

with open('capstone3.pkl', 'rb') as pickle_in:
    model = pickle.load(pickle_in)
import pandas as pd
def prediction(df):
    return model.predict(df)

def main():
    st.write("""
    # Cancer Type Prediction App based on text
""")
    st.header("User Input")
    x=st.text_input("Enter Text")
    data={"Text":x}
    df=pd.DataFrame(data,index=[0])
    
    if st.button("Predict"):
        
        result = prediction(df)
        if result==0:
            category="Thyroid Cancer"
        elif result==1:
            category="Colon Cancer"
        elif result==2:
            category="Lung Cancer"  
        else:
            print("Out of context text")          
        st.success('The category is {}'.format(category))
        
    st.write("Result")
    st.write(prediction)

if __name__=="__main__":
    main()

