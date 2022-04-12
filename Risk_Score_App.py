import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


st.image(
    "https://cca.uel.edu.vn/Resources/Images/SubDomain/cca/UEL%20Brand%20Toolkit/UEL%20-%20logo%20official.png",
    width=100,
)
st.write("""
# Risk Tolerance Score Prediction App
This app uses ML model to predict the **Risk Tolerance** score!
Data obtained from **UEL-ers** in Python by ***Group 35*** from a survey with more than 500 responses of participants in Ho Chi Minh City.
""")

#st.image("https://www.plan-wisely.com/wp-content/uploads/sites/2/2020/07/Risk.png",
#    width=700,)
image = Image.open('NGHIÊN CỨU KHOA HỌC (1).png')
st.image(image, caption='Members of Group 35', width=700)

st.sidebar.subheader('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://docs.google.com/spreadsheets/d/192iJyTBJWstQ3ReTLvqMUXBSemrfJLuFHJSzwb_6rU0/edit?usp=sharing)
""")
st.write('---')

# Display definition in layout 
with st.beta_expander("What is Risk Tolerance?"):
    st.markdown('**Risk tolerance** is the degree of variability in investment returns that an investor is willing to withstand in their financial planning.')
    st.image(
    "https://www.tnex.com.vn/wp-content/uploads/2021/10/7s-01-800x400.png",
    width=700,
)
    st.markdown('Risk tolerance is an important component in investing. You should have a realistic understanding of your ability and willingness to stomach large swings in the value of your investments; if you take on too much risk, you might panic and sell at the wrong time.')
   
with st.beta_expander("Factors affecting the Risk Tolerance"):
    st.markdown('It looks at how much market risk—stock volatility, stock market swings, economic or political events, regulatory, or interest rate changes—an investor can tolerate, considering that all of these factors might cause their portfolio to slide.')
    st.image(
    "https://cdn.sketchbubble.com/pub/media/catalog/product/optimized1/c/1/c11a79860b06dd7be52599bdc8aa0c8a56b4c90521c8a7ef15aac3b291a8794f/risk-tolerance-slide3.png",
    width=700,
)
    st.markdown("A person's age, investment goals, income, and comfort level all play into determining their risk tolerance.")
        
with st.beta_expander("Levels"):
    st.image(
    "https://img.etimg.com/photo/49085549.cms",
    width=500,clamp = True,
)
    st.subheader('Score:  0 – 18')
    st.markdown(' Conservative tolerance for risk')
    st.subheader('Score:  19 – 32')
    st.markdown(' Average/moderate tolerance for risk')
    st.subheader('Score:  33 – 47')
    st.markdown(' Aggressive tolerance for risk')

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        st.header('Please fill-in all required information')
        Age = st.selectbox('Age: Bạn bao nhiêu tuổi rồi ?',('A. <18 tuổi','B. 18-25 tuổi','C. >25 tuổi'))
        st.write('You selected:', Age)
        Gender = st.selectbox('Gender: Giới tính của bạn ?',('A. Nam','B. Nữ'))
        st.write('You selected:', Gender)
        Marital = st.selectbox('Marital: Tình trạng hôn nhân của bạn ?',('A. Độc thân\n(chưa kết hôn hoặc đã ly hôn)','B. Đã kết hôn'))
        st.write('You selected:', Marital)
        Income = st.selectbox('Income: **Thu nhập cá nhân hàng tháng của bạn nằm trong khoảng nào ?**',('A. <3tr','B. 3tr-12tr','C. >12tr'))
        st.write('You selected:', Income)
        Ratio = st.selectbox('Ratio: Bạn dành bao nhiêu phần trăm trong thu nhập để phục vụ cho mục đích đầu tư ?',('A. <3tr','B. 3tr-12tr','C. >12tr'))
        st.write('You selected:', Ratio)
        Education = st.selectbox('Education: Trình độ học vấn của bạn ?',('A. Dưới đại học.','B. Đại học.','C. Sau đại học\n(thạc sĩ, tiến sĩ hoặc cao hơn).'))
        st.write('You selected:', Education)
        Profession = st.selectbox('Profession: Bạn đánh giá về kiến thức trong đầu tư của bạn thế nào ?',('A. Không có/chưa có bất kỳ kinh\nnghiệm trong lĩnh vực đầu tư.','B. Có ít kiến thức trong đầu tư.\nChủ yếu học hỏi qua sách báo, Internet.','C. Có nhiều kiến thức đầu tư,\nđã/đang hoạt động trong lĩnh vực liên quan đến đầu tư.'))
        st.write('You selected:', Profession)
        Optimism = st.selectbox('Optimism: Bạn mong muốn mình sẽ là trường hợp nào trong 2 trường hợp sau ?',('A. Lợi suất nhận được từ các\nkhoản đầu tư cao hơn ngân hàng một chút, ổn định.','B. Lợi suất nhận được từ các\nkhoản đầu tư có thể lỗ nhiều hoặc lãi nhiều, không ổn định.'))
        st.write('You selected:', Optimism)
        Objective = st.selectbox('Source: Nguồn thu nhập chính của bạn là gì ?',('A. Lương công việc chính.**','B. Đầu tư.','C. Khác.'))
        st.write('You selected:', Objective)
        data = {'Age': Age.split('.')[0],
                'Gender': Gender.split('.')[0],
                'Marital': Marital.split('.')[0],
                'Income': Income.split('.')[0],
                'Ratio': Ratio.split('.')[0],
                'Education': Education.split('.')[0],
                'Profession': Profession.split('.')[0],
                'Optimism': Optimism.split('.')[0],
                'Objective': Objective.split('.')[0]}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('data_raw.csv')
penguins = penguins_raw.drop(columns=['Score','Unnamed: 0'])
df = pd.concat([input_df,penguins],axis=0)

# Encoding of ordinal features
encode = ['Age','Gender','Marital','Income','Ratio','Education','Profession','Optimism','Objective']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)



# Reads in saved Regression model
load_clf = pickle.load(open('model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)

st.header('Prediction of Risk Tolerance Score')
st.info(prediction.round(decimals=1))
st.markdown('---')

def classify(prediction):
    if load_clf.predict(df) <= 18:
        st.info("Conservative tolerance for risk")
    elif load_clf.predict(df) >= 19 and load_clf.predict(df)<=32:
        st.info("Average/moderate tolerance for risk")     
    else:
        st.info(" Aggressive tolerance for risk")
        
st.header('Level')
classify(prediction)
st.markdown('---')
