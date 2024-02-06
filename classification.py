import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split 

df = pd.read_csv ("https://sololearn.com/uploads/files/titanic.csv")
df['male'] = df['Sex'] == 'male'

X = df[['Fare','Age','Pclass','Siblings/Spouses','Parents/Children','male']].values
y = df['Survived'].values 

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 27)

model = LogisticRegression ()
model.fit(X_train,y_train)

y_pred = model.predict_proba(X_test)[:,1] > 0.75

print(model.score(X,y))
print("recall",recall_score(y_test,y_pred))
print('precision',precision_score(y_test,y_pred))