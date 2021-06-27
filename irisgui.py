#load the iris data set to program
import tkinter.messagebox as m
from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
Y=iris.target
########split the dataset for training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=5)
def knn():
    global acc_knn
    global K
    ###create a model KNN --KNearest neighbors  algorithm
    from sklearn.neighbors import KNeighborsClassifier
    K=KNeighborsClassifier(n_neighbors=7)
    ####train the model  by using training dataset
    K.fit(X_train,Y_train)
    ###test the model  by using testing dataset
    Y_pred_knn=K.predict(X_test)
    #find accuracy
    from sklearn.metrics import accuracy_score
    acc_knn=accuracy_score(Y_test,Y_pred_knn)
    acc_knn=round(acc_knn*100,2)
    m.showinfo(title="KNN",\
               message="accuracy is"+str(acc_knn)+"%")
def lg():
    global acc_lg
    global L
    from sklearn.linear_model import LogisticRegression
    L=LogisticRegression(solver='liblinear',multi_class='auto')
    #train the model
    L.fit(X_train,Y_train)
    #test the model
    Y_pred_lg=L.predict(X_test)
    #find accuracy
    from sklearn.metrics import accuracy_score
    acc_lg=accuracy_score(Y_test,Y_pred_lg)
    acc_lg=round(acc_lg*100,2)
    m.showinfo(title="LG",\
               message="accuracy is"+str(acc_lg)+"%")
def dt():
    global acc_dt
    global D
    from sklearn.tree import DecisionTreeClassifier
    D=DecisionTreeClassifier()
    ##train the model
    D.fit(X_train,Y_train)
    #test the model
    Y_pred_dt=D.predict(X_test)
    #finfd accuracy
    from sklearn.metrics import accuracy_score
    acc_dt=accuracy_score(Y_test,Y_pred_dt)
    acc_dt=round(acc_dt*100,2)
    m.showinfo(title="DT",\
               message="accuracy is"+str(acc_dt)+"%")
def nb():
    global acc_nb
    global N
    from sklearn.naive_bayes import GaussianNB
    N=GaussianNB()
    #train the model
    N.fit(X_train,Y_train)
    #test the model
    Y_pred_nb=N.predict(X_test)
    #find accuracy
    from sklearn.metrics import accuracy_score
    acc_nb=accuracy_score(Y_test,Y_pred_nb)
    acc_nb=round(acc_nb*100,2)
    m.showinfo(title="NB",\
               message="accuracy is"+str(acc_nb)+"%")
def compare():
    import matplotlib.pyplot as plt
    model=['knn','lg','dt','nb']
    accuracy=[acc_knn,acc_lg,acc_dt,acc_nb]
    plt.bar(model,accuracy,color=['green','yellow','cyan','orange'])
    plt.xlabel("MODELS")
    plt.ylabel("ACCURACY")
    plt.show()
def submit():
    global K
    global L
    global D
    global N
    global acc_knn
    global acc_dt
    global acc_nb
    global acc_lg
    acc=[acc_knn,acc_lg,acc_nb,acc_dt]
    if acc_knn==max(acc):
        bestmodel=K
    elif acc_lg==max(acc):
        bestmodel=L
    elif acc_dt==max(acc):
        bestmodel=D
    else:
        bestmodel=N
    sl=float(vsl.get())
    sw=float(vsw.get())
    pi=float(vpl.get())
    pw=float(vpw.get())
    result=bestmodel.predict([[sl,sw,pl,pw]])
    if result[0]==0:
        flower="setosa"
    elif result[0]==1:
        flower="versicolor"
    else:
        flower="virginicia"
    m.showinfo(title="IRIS",message=flower)    
    

def reset():
    vsl.set("")
    vsw.set("")
    vpl.set("")
    vpw.set("")
    
    
    


####################################################
####create  the gui
from tkinter import *
w=Tk()
La=Label(w,text="IRIS FLOWER PREDICTION",bg='cyan')
Bknn=Button(w,text="KNN",command=knn)
Blg=Button(w,text="LG",command=lg)
Bdt=Button(w,text="DT",command=dt)
Bnb=Button(w,text="NB",command=nb)
Bcmp=Button(w,text="COMPARE",command=compare)
Lb=Label(w,text="Predict for a new flower",bg='yellow')
Lsl=Label(w,text="sepal length")
Lsw=Label(w,text="sepal width")
Lpl=Label(w,text="petal length")
Lpw=Label(w,text="petal length")
Esl=Entry(w,width=10)
Esw=Entry(w,width=10)
Epl=Entry(w,width=10)
Epw=Entry(w,width=10)
Bsubmit=Button(w,text="submit",command=submit)
Breset=Button(w,text="reset",command=reset)
###########33place components
La.grid(row=1,column=1,columnspan=4)
Bknn.grid(row=2,column=1)
Blg.grid(row=2,column=2)
Bdt.grid(row=2,column=3)
Bnb.grid(row=2,column=4)
Bcmp.grid(row=3,column=2,columnspan=2)
Lb.grid(row=4,column=1,columnspan=4)
Lsl.grid(row=5,column=1)
Esl.grid(row=5,column=2) 
Lsw.grid(row=5,column=3)
Esw.grid(row=5,column=4)
##
Lpl.grid(row=6,column=1)
Epl.grid(row=6,column=2)
Lpw.grid(row=6,column=3)
Epw.grid(row=6,column=4)
Bsubmit.grid(row=7,column=1,columnspan=2)
Breset.grid(row=7,column=3,columnspan=2)
w.mainloop()
