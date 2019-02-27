import pandas as pd

df=pd.read_csv(r'C:\Users\wfw\Desktop\parms1.csv')
# print(df)
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())

import matplotlib.pyplot as plt
# df.hist(bins=50)
# plt.show()

#计算关联
corr_matrix = df.corr()
#价格为因变量
print(corr_matrix['price'].sort_values(ascending=False)) #0.816310

#散点图
df.plot(kind="scatter", x="key_num",y="price")
# plt.show()


#用sklearn将数据分成训练数据和测试数据
from sklearn.model_selection import train_test_split
train_set,test_set=train_test_split(df,test_size=0.25,random_state=42)
# print(train_set)

#训练数据
x_train=train_set.drop('price',axis=1)
y_train=train_set['price'].copy()

#数据归一化
from sklearn.preprocessing import StandardScaler
standardscaler=StandardScaler()
data1=standardscaler.fit_transform(x_train)
# print(ss)
x_train=pd.DataFrame(data1,columns=['key_num','key_add','tx_count','fee']) #归一化后的数据
# print(ss)


#线性回归
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x_train,y_train)

#测试数据
x_test=test_set.drop('price',axis=1)
y_test=test_set['price'].copy()

# 归一化
data2=standardscaler.fit_transform(x_test)
x_test=pd.DataFrame(data2,columns=['key_num','key_add','tx_count','fee']) #归一化后的数据

#查看预测误差
import numpy as np
from sklearn.metrics import mean_squared_error
prediction=lin_reg.predict(x_test)
lin_mse=mean_squared_error(y_test,prediction)
lin_rmse=np.sqrt(lin_mse)
print(y_test.tolist()[80:100])
print(prediction.tolist()[80:100])
print('线性回归均方差:%f'%lin_rmse)


#决策树
from sklearn.tree import DecisionTreeRegressor
tree_reg=DecisionTreeRegressor()
tree_reg.fit(x_train,y_train)

prediction=tree_reg.predict(x_test)
tree_mse=mean_squared_error(y_test,prediction)
tree_rmse=np.sqrt(tree_mse)
print(y_test.tolist()[80:100])
print(prediction.tolist()[80:100])
print('决策树均方差:%f'%tree_rmse)


# #十折交叉验证
from sklearn.model_selection import cross_val_score
# scores=cross_val_score(tree_reg,x_train,y_train,
#                        scoring="neg_mean_squared_error", cv=10)#越大越好
#
# rmse_scores = np.sqrt(-scores)
# print(rmse_scores)
#
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())

# display_scores(rmse_scores)


#svm回归
from sklearn import svm
svm_reg = svm.SVR()
svm_reg.fit(x_train,y_train)
prediction=svm_reg.predict(x_test)
svm_mse=mean_squared_error(y_test,prediction)
rf_rmse=np.sqrt(svm_mse)
print(y_test.tolist()[80:100])
print(prediction.tolist()[80:100])
print('svm均方差:%f'%rf_rmse)



#随机森林
from sklearn.ensemble import RandomForestRegressor
# rf_reg=RandomForestRegressor(n_estimators=150)
rf_reg=RandomForestRegressor(n_estimators=200,max_features=2)
rf_reg.fit(x_train,y_train)

prediction=rf_reg.predict(x_test)
rf_mse=mean_squared_error(y_test,prediction)
rf_rmse=np.sqrt(rf_mse)
print(y_test.tolist()[80:100])
print(prediction.tolist()[80:100])
print('随机森林均方差:%f'%rf_rmse)

# 交叉验证
scores=cross_val_score(rf_reg,x_train,y_train,
                       scoring="neg_mean_squared_error", cv=10)#越大越好
rf_rmse_scores = np.sqrt(-scores)
display_scores(rf_rmse_scores)


#网格搜索
from sklearn.model_selection import RandomizedSearchCV
# forest_reg = RandomForestRegressor()
# param_grid={'n_estimators':[3,10,30,60,90,150,200,250,300,350,400,450,500],
#             # 'max_depth':[2,3,4,5]}
#             'max_features':[1,2,3,4]}
# random_grid_search = RandomizedSearchCV(forest_reg,param_grid,
#                                         n_iter=1,cv=10,scoring='neg_mean_squared_error')
# random_grid_search.fit(x_train,y_train)
# rf_rmse_scores = np.sqrt(-random_grid_search.best_score_)
#
# print(rf_rmse_scores)
# print(random_grid_search.best_params_)
#
#
#
# from sklearn.externals import joblib
# # clf=random_grid_search.best_estimator_
# # joblib.dump(clf, r'E:\pythontest\model.pkl',compress=3)
#
#
# clf=joblib.load(r'E:\pythontest\model.pkl')
# result=clf.predict(x_test)
# rf_mse=mean_squared_error(y_test,result)
# rf_rmse=np.sqrt(rf_mse)
# print(rf_rmse)