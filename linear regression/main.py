import pandas as pd 
import matplotlib.pyplot as plt

data= pd.read_csv("file.csv")

# plt.scatter(data.study_time,data.score)
# plt.show()

def loss_function(m,b,points):
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].study_time
        y=points.iloc[i].score
        total_error+=(y-(m*x+b))**2
    return total_error/float(len(points))

def gradient_decent(m_now,b_now,points,l):
    m_gradient=0
    b_gradient=0
    n=len(points)

    for i in range(n):
        x=points.iloc[i].study_time
        y=points.iloc[i].score

        m_gradient+= -(2/n) *x* (y -(m_now*x + b_now))
        b_gradient+= -(2/n) * (y-(m_now*x +b_now))

    
    m =m_now -l*m_gradient
    b= b_now -l*b_gradient

    return m,b

m=0
b=0
l=0.0001
epoch=200

for i in range(epoch):

    if i%50==0:
        print(i)
    
    m,b=gradient_decent(m,b,data,l)
print(m,b)

plt.scatter(data.study_time,data.score,color="black")
plt.plot(range(10,30), [m*x+b for x in range(10,30)],color="red")
plt.show()
        