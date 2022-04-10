import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

from sklearn import neighbors
import statsmodels.formula.api as smf

df_full = pd.read_csv('C:/Users/ACER/FINAL.csv')
df_full = df_full.drop('Unnamed: 0',axis=1)
df_1 = df_full.loc[:,'Age':'Objective']
df_2 = df_full.loc[:,'GL_1':]
df_2['GL_1']=df_2['GL_1'].apply(lambda x: x.replace('A','4').replace('B','3').replace('C','2').replace('D','1'))
df_2['GL_2']=df_2['GL_2'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
df_2['GL_3']=df_2['GL_3'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
df_2['GL_4']=df_2['GL_4'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3'))
df_2['GL_5']=df_2['GL_5'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3'))
df_2['GL_6']=df_2['GL_6'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
df_2['GL_7']=df_2['GL_7'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
df_2['GL_8']=df_2['GL_8'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
df_2['GL_9']=df_2['GL_9'].apply(lambda x: x.replace('A','1').replace('B','3'))
df_2['GL_10']=df_2['GL_10'].apply(lambda x: x.replace('A','1').replace('B','3'))
df_2['GL_11']=df_2['GL_11'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
df_2['GL_12']=df_2['GL_12'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3'))
df_2['GL_13']=df_2['GL_13'].apply(lambda x: x.replace('A','1').replace('B','2').replace('C','3').replace('D','4'))
for i in df_2.columns.tolist():
    df_2[i] = df_2[i].apply(lambda x: int(x))
df_1['Score'] = 0
for i in range(df_2.shape[0]):
    df_1['Score'].iloc[i,:]=sum(df_2.iloc[i,:])
df=df_1.copy()
df=pd.get_dummies(df)


# Separating X and y
X=df.drop(['Score','Experience_A','Experience_B','Experience_C','Experience_D',
           'Experience_E','Experience_F','Experience_G','Experience_H'],axis=1)
y=df['Score']


# Build random forest model
rs=70
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=rs)
# clf = RandomForestClassifier()
# clf.fit(X, Y)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
neighbors = []
error = []
for i in range(1,101):
    neighbors.append(i)
    knn_model = KNeighborsRegressor(n_neighbors=i,weights = 'distance')
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    error.append(mean_absolute_error(y_test,y_pred_knn))
err = tuple(zip(neighbors,error))
df_err = pd.DataFrame(err, columns = ['neighbors','error'])
df_err[df_err.error == min(df_err.error)]
for i in range(len(error)):
    if error[i-1] == min(error):
        t=i

clf = KNeighborsRegressor(n_neighbors=26,weights = 'distance')
clf.fit(X_train, y_train)


def evaluatemodel(true,predicted,modelname):
    MAE = round(mean_absolute_error(true,predicted),3)
    print("\tMAE:", MAE)
    
y_pred_knn = knn_model.predict(X_test)
evaluatemodel(y_test,y_pred_knn,'K-Nearest Neighbors')



# Saving the model
import pickle
pickle.dump(clf, open('model.pkl', 'wb'))


#******************************************************************************#
