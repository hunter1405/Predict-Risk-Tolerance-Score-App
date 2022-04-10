import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.write("""
# Risk Tolerance Score Prediction App
This app predicts the **Risk Tolerance** score!
Data obtained from UEL-ers in Python by ***Group 35***.
""")

st.sidebar.subheader('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://docs.google.com/spreadsheets/d/192iJyTBJWstQ3ReTLvqMUXBSemrfJLuFHJSzwb_6rU0/edit?usp=sharing)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        Age = st.sidebar.selectbox('Age',('A','B','C'))
        Gender = st.sidebar.selectbox('Gender',('A','B'))
        Marital = st.sidebar.selectbox('Marital',('A','B'))
        Income = st.sidebar.selectbox('Income',('A','B','C'))
        Ratio = st.sidebar.selectbox('Ratio',('A','B','C'))
        Education = st.sidebar.selectbox('Education',('A','B','C'))
        Profession = st.sidebar.selectbox('Profession',('A','B','C'))
        Optimism = st.sidebar.selectbox('Optimism',('A','B'))
        Objective = st.sidebar.selectbox('Source',('A','B','C'))
        data = {'Age': Age,
                'Gender': Gender,
                'Marital': Marital,
                'Income': Income,
                'Ratio': Education,
                'Profession': Profession,
                'Optimism': Optimism,
                'Objective': Objective}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('C:/Users/ACER/data_raw.csv')
penguins = penguins_raw.drop(columns=['Score','Unnamed: 0'])
df = pd.concat([input_df,penguins],axis=0)

# Encoding of ordinal features
encode = ['Age','Gender','Marital','Income','Ratio','Education','Profession','Optimism','Objective']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)

# Displays the user input features
st.header('Questions')
st.subheader('Age: Bạn bao nhiêu tuổi rồi ?')
st.markdown('  A. <18 tuổi')
st.markdown('  B. 18-25 tuổi')
st.markdown('  C. <18 tuổi')

st.subheader('Gender: Giới tính của bạn ?')
st.markdown('  A. Nam')
st.markdown('  B. Nữ')

st.subheader('Marital: Tình trạng hôn nhân của bạn ?')
st.markdown('  A. Độc thân (chưa kết hôn hoặc đã ly hôn)')
st.markdown('  B. Đã kết hôn')

st.subheader('Income: Thu nhập cá nhân hàng tháng của bạn nằm trong khoảng nào ?')
st.markdown('  A. <3tr')
st.markdown('  B. 3tr-12tr')
st.markdown('  C. >12tr')

st.subheader('Ratio: Bạn dành bao nhiêu phần trăm trong thu nhập để phục vụ cho mục đích đầu tư ?')
st.markdown('  A. <20%')
st.markdown('  B. 20%-50%')
st.markdown('  C. >50%')

st.subheader('Education: Trình độ học vấn của bạn ?')
st.markdown('  A. Dưới đại học.')
st.markdown('  B. Đại học.')
st.markdown(' C. Sau đại học (thạc sĩ, tiến sĩ hoặc cao hơn).')

st.subheader('Profession: Bạn đánh giá về kiến thức trong đầu tư của bạn thế nào?')
st.markdown('  A. Không có/chưa có bất kỳ kinh nghiệm trong lĩnh vực đầu tư.')
st.markdown('  B. Có ít kiến thức trong đầu tư. Chủ yếu học hỏi qua sách báo, Internet.')
st.markdown('  C. Có nhiều kiến thức đầu tư, đã/đang hoạt động trong lĩnh vực liên quan đến đầu tư')

st.subheader('Optimism: Bạn mong muốn mình sẽ là trường hợp nào trong 2 trường hợp sau ?')
st.markdown('  A. Lợi suất nhận được từ các khoản đầu tư cao hơn ngân hàng một chút, ổn định.')
st.markdown('  B. Lợi suất nhận được từ các khoản đầu tư có thể lỗ nhiều hoặc lãi nhiều, không ổn định.')

st.subheader('Source: Nguồn thu nhập chính của bạn là gì ?')
st.markdown('  A. Lương công việc chính.')
st.markdown('  B. Đầu tư.')
st.markdown('  C. Khác.')



st.title('User Input features')



if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Reads in saved classification model
load_clf = pickle.load(open('model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)


st.header('Prediction of Risk Tolerance Score')
st.write(prediction)
st.write('---')

def classify(prediction):
    if load_clf.predict(df) <= 18:
        st.write("Low tolerance for risk")
    elif load_clf.predict(df) >= 19 and load_clf.predict(df)<=22:
        st.write("Below-average tolerance for risk")
    elif load_clf.predict(df) >= 23 and load_clf.predict(df)<=28:
           st.write("Average/moderate tolerance for risk")
    elif load_clf.predict(df) >= 29 and load_clf.predict(df)<=32:
           st.write("Above-average tolerance for risk")         
    else:
        st.write("High tolerance for risk")
        
st.header('Level')
classify(prediction)
st.write('---')
