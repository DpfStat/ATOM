import sklearn
from sklearn.linear_model import Perceptron
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
df['label']=iris.target
df.columns = [
    'sepal length', 'sepal width', 'petal length', 'petal width', 'label'
]
df.label.value_counts()

data = np.array(df.iloc[:100, [0, 1, -1]])
X, y = data[:,:-1], data[:,-1]
y = np.array([1 if i == 1 else -1 for i in y])

clf = Perceptron(fit_intercept = True,
                 max_iter = 1000,
                 shuffle = True)
clf.fit(X,y)

# get the weights assigned to the features
print(clf.coef_)
# intercept
print(clf.intercept_)

plt.figure(figsize =(10, 10))
plt.scatter(data[:50, 0], data[:50, 1], c='b', label='Iris-setosa',)
plt.scatter(data[50:100, 0], data[50:100, 1], c='orange', label='Iris-versicolor')
x_ponits = np.arange(4, 8)
y_ = -(clf.coef_[0][0]*x_ponits + clf.intercept_)/clf.coef_[0][1]
plt.plot(x_ponits, y_)

plt.legend()
plt.grid(False)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend()
plt.show()

#clf = Perceptron(fit_intercept = True,
#                 max_iter = 1000,
#                 tol = None,
#                 shuffle = True)
# tol is the argument to decide when to stop, tol = 0.001 for the default
