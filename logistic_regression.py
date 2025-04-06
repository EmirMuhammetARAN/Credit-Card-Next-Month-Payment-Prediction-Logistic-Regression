import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('card.csv')

df.head(3)

df=df.drop("ID",axis=1)

y=df["default.payment.next.month"]
x=df.drop("default.payment.next.month",axis=1)

df.shape

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.77,random_state=6)

log=LogisticRegression()
model=log.fit(x_train,y_train)

model.score(x_test,y_test)

denemex=np.array(x.iloc[1903])

model.predict([denemex])

y.iloc[1903]