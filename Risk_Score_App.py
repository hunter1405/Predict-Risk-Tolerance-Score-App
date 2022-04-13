import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

st.set_page_config(page_title='Risk Tolerance Prediction',page_icon="3️⃣5️⃣",layout="wide")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://www.uel.edu.vn" target="_blank">
  <img class="image-25"src="https://www.uel.edu.vn/Resources/Images/SubDomain/HomePage/Style/logo_uel.png" width="350"
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

h = st.markdown("""
<style>
div.fullScreenFrame > div {
    display: flex;
    justify-content: center;
}
</style>""", unsafe_allow_html=True)

#Title
original_title = '<p style="text-align: center; color:#3498DB; text-shadow: 2px 2px 4px #000000; font-size: 60px;">Risk Tolerance Score Prediction App</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.write("""This app uses ML model to predict the **Risk Tolerance** score!
Data obtained from **UEL-ers** in Python by ***Group 35*** from a survey with more than 500 responses of participants in Ho Chi Minh City.""")

#col1, col2, col3 = st.columns(3)
#with col1:
 #   st.write(' ')
#with col2:
#    image = Image.open('NGHIÊN CỨU KHOA HỌC (1).png')
 #   st.image(image, caption='Members of Group 35')
#with col3:
 #  st.write('   ')
  
background = Image.open("NGHIÊN CỨU KHOA HỌC (1).png")
col1, col2, col3 = st.columns([0.2, 1, 0.2])
col2.image(background, use_column_width=True)
    
st.write('---')

# Display definition in layout 
with st.expander("What is Risk Tolerance?"):
    st.markdown('**Risk tolerance** is the degree of variability in investment returns that an investor is willing to withstand in their financial planning.')
    st.image(
    "https://www.tnex.com.vn/wp-content/uploads/2021/10/7s-01-800x400.png",
    width=800,
)
    st.markdown('Risk tolerance is an important component in investing. You should have a realistic understanding of your ability and willingness to stomach large swings in the value of your investments; if you take on too much risk, you might panic and sell at the wrong time.')
   
with st.expander("Factors affecting the Risk Tolerance"):
    st.markdown('It looks at how much market risk—stock volatility, stock market swings, economic or political events, regulatory, or interest rate changes—an investor can tolerate, considering that all of these factors might cause their portfolio to slide.')
    st.image(
    "https://cdn.sketchbubble.com/pub/media/catalog/product/optimized1/c/1/c11a79860b06dd7be52599bdc8aa0c8a56b4c90521c8a7ef15aac3b291a8794f/risk-tolerance-slide3.png",
    width=800,
)
    st.markdown("A person's age, investment goals, income, and comfort level all play into determining their risk tolerance.")
        
with st.expander("Levels"):
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
# Set up the checkbox
l = st.markdown("""
<style>
body {
    color: #fff;
}
div.row-widget.stRadio > div {
    flex-direction: column;
    align-items: stretch;
}
div.row-widget.stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
    background-color: cornflowerblue;
}
</style>""", unsafe_allow_html=True)     
# Collects user input features into dataframe
def user_input_features():
        st.header('Please fill-in all required information in Vietnamese')
        st.subheader('Bạn bao nhiêu tuổi rồi ?')
        Age = st.radio('',('A. <18 tuổi','B. 18-25 tuổi','C. >25 tuổi'))
        st.write('You selected:', Age.split('.')[1])
        st.subheader('Giới tính của bạn ?')
        Gender = st.radio('',('A. Nam','B. Nữ'))
        st.write('You selected:', Gender.split('.')[1])
        st.subheader('Tình trạng hôn nhân của bạn ?')
        Marital = st.radio('',('A. Độc thân\n(chưa kết hôn hoặc đã ly hôn)','B. Đã kết hôn'))
        st.write('You selected:', Marital.split('.')[1])
        st.subheader('Thu nhập cá nhân hàng tháng của bạn nằm trong khoảng nào ?')
        Income = st.radio('',('A. <3tr','B. 3tr-12tr','C. >12tr'))
        st.write('You selected:', Income.split('.')[1])
        st.subheader('Bạn dành bao nhiêu phần trăm trong thu nhập để phục vụ cho mục đích đầu tư ?')
        Ratio = st.radio('',('A. <20%','B. 20%-50%','C. >50%'))
        st.write('You selected:', Ratio.split('.')[1])
        st.subheader('Trình độ học vấn của bạn ?')
        Education = st.radio('',('A. Dưới đại học.','B. Đại học.','C. Sau đại học\n(thạc sĩ, tiến sĩ hoặc cao hơn).'))
        st.write('You selected:', Education.split('.')[1])
        st.subheader('Bạn đánh giá về kiến thức trong đầu tư của bạn thế nào ?')
        Profession = st.radio('',('A. Không có/chưa có bất kỳ kinh\nnghiệm trong lĩnh vực đầu tư.','B. Có ít kiến thức trong đầu tư.\nChủ yếu học hỏi qua sách báo, Internet.','C. Có nhiều kiến thức đầu tư,\nđã/đang hoạt động trong lĩnh vực liên quan đến đầu tư.'))
        st.write('You selected:', Profession.split('.')[1])
        st.subheader('Bạn mong muốn mình sẽ là trường hợp nào trong 2 trường hợp sau ?')
        Optimism = st.radio('',('A. Lợi suất nhận được từ các\nkhoản đầu tư cao hơn ngân hàng một chút, ổn định.','B. Lợi suất nhận được từ các\nkhoản đầu tư có thể lỗ nhiều hoặc lãi nhiều, không ổn định.'))
        st.write('You selected:', Optimism.split('.')[1])
        st.subheader('Nguồn thu nhập chính của bạn là gì ?')
        Objective = st.radio('',('A. Lương công việc chính.','B. Đầu tư.','C. Khác.'))
        st.write('You selected:', Objective.split('.')[1])
            
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
prediction = load_clf.predict(df).round(decimals=1)

m = st.markdown("""
<style>
div.stButton > button:first-child {
background-color: #3498DB;color:white;font-size:20px;height:3em;width:30em;border-radius:10px 10px 10px 10px;
}
</style>""", unsafe_allow_html=True)

if st.button("Submit this form"):
    st.header('Prediction of Risk Tolerance Score')
    st.info(prediction)

    def classify(prediction):
        if load_clf.predict(df) <= 18:
            st.info("Conservative tolerance for risk")
        elif load_clf.predict(df) >= 19 and load_clf.predict(df)<=32:
            st.info("Average/moderate tolerance for risk")     
        else:
            st.info(" Aggressive tolerance for risk")
   
    def reccomend(prediction):
        if load_clf.predict(df) <= 18:
            st.info("For a Conservative level, we recommend an investment channel with low volatility, aiming at capital adequacy, and protecting capital from the impact of inflation. The preferable investment channel for you are: **gold**, **savings**, **dollars**")
        elif load_clf.predict(df) >= 19 and load_clf.predict(df)<=32:
            st.info("For a Average/moderate level, we recommend an investment channel with growth potential. The preferable investment channel for you are: **stocks**, **real estate**")     
        else:
            st.info("For a Aggressive level, we recommend a high-risk investment channel with high volatility in the short, medium and long term. However, the return can be significantly higher than the inflation rate. The right investment channel for you are: **stock**, **commodity markets**, **money markets**") 
    st.header('Level')
    classify(prediction)
    st.header('Reccommendation')
    reccomend(prediction)

else:
    st.header('Prediction of Risk Tolerance Score')
    st.info("Missing information")
    st.header('Level')
    st.info("Missing information")
    st.header('Reccommendation')
    st.info("Missing information")

st.markdown('---')
