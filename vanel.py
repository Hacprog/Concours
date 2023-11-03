
#import matplotlib.pyplot as plt
#import numpy as np
#A = np.array([[1, 2],[2, 4]])
#b = np.array([3, 5])
#c = 6 
#x = np.linspace(-10, 10, 100)
#y = np.linspace(-10, 10, 100)
#X,Y = np.meshgrid(x, y)
#Z = A[0, 0]*X**2+(A[0, 1]+A[1, 0])*X*Y+A[1, 1]*Y**2+b[0]*X+b[1]*Y+c
#fig=plt.figure()
#ax=fig.add_subplot(111,projection='3d')
#ax.plot_surface(X,Y,Z)
#plt.show()
import matplotlib.pyplot as plt
labels = ['echec','reussite','passable','prometteur']
sizes = [15, 37, 42, 10]
colors = ['red','blue','yellow','green']
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels,colors=colors,autopct='%1.1f%%',startangle=90)
ax.set_title('mon diagramme circulaire')
plt.show()