#Попытка номер 2
import matplotlib as mpl
import math
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets

def data_read(path_to_data):
        koordinaty=[]
        X_list=[]
        Y_list=[]
        input_file=open(path_to_data, 'r',encoding= 'utf-8')
        red_data=input_file.readlines()
        #print(red_data)
        input_file.close()
       
        if len (red_data) >0:
            print("я открыл файл")    
            for line in range(len(red_data)):
                if line ==1:
                    header = (red_data[line].replace('\n','' )).split('\t')

                    one_column = None
                    two_column = None

                    for position in range(len(header)):

                        if header[position] == 'x':
                            one_column = position

                        if header[position] == 'y':
                            two_column = position
                if line > 1:
                    data_line = (red_data[line].replace('\n','' )).split('\t')
                    if len(data_line) == len(header):
                        X_list.append(float(data_line[one_column]))
                        Y_list.append(float(data_line[two_column]))
        else:
                print('что то не так')
        koordinaty.append(X_list)
        koordinaty.append(Y_list)
        return koordinaty
   
        #print("Это реально работает!!!")
def plot_graph_smart_0():
            
            miks=[]
            miks.append(fig)
            miks.append(axes)
            #plt.show()
            return miks
def plot_graph_smart_1(file_path):            
            koordinaty_X,koordinaty_Y = data_read(file_path)
            fig,axes=plt.subplots(nrows=1,ncols=1,figsize=(4,4))    
            axes.grid(True,c='lightgrey',alpha=0.5)
            axes.plot(koordinaty_X,koordinaty_Y)
            #plt.show()
            return fig
def filter_red(X,Y):
        x_r=[]
        y_r=[]
        x=X
        y=Y
        x_min=[]
        x_max=[]
        y_min=[]
        y_max=[]
        summ=0
        for i in range(len(x)):
                if x[i]>=600 and x[i]<=700:
                      x_r.append(x[i])
                      y_r.append(y[i])

                      
        '''==============='''

        if x_r!=[]:
                if min(x_r)!=600 :
                        for i in range(len(x)):
                                if x[i]<600:
                                    x_min.append(x[i])
                                    y_min.append(y[i])
                        z=(x_min.index(max(x_min)))
                        xn=x_min[z]
                        yn=y_min[z]
        
                        #print(max(x_min))
                        #print('index = ',z)
                        #print(yn)

                        z=x_r.index(min(x_r))
                        xz=x_r[z]
                        yz=y_r[z]
                        #print('xmax = ',xz)
                        #print('ymax = ',yz)
        
                        yx=(((600-xn)*(yz-yn))/(xz-xn))+yn
                        #print('rezult = ',y)
                 
                        x_r.insert(0,600)
                        y_r.insert(0,yx)              #Переобозначил т.к повторно обращаюся  к массиву y[i]
                        print(x_r)
                        print(y_r)
                        x_min.clear()
                        y_min.clear()
                        #print(y_min)

        
                '''==============='''
                if max(x)>700 and max(x_r)!=700:
                        xn=max(x_r)
                        z=x_r.index(max(x_r))
                        #print("red border = ",z)
                        yn=y_r[z]
                        for i in range(len(x)):
                                if x[i]>700:
                                        x_min.append(x[i])
                                        y_min.append(y[i])
                        xz=min(x_min)
                        z=x_min.index(min(x_min))
                        yz=y_min[z]
                        #print('xz = ',xz)
                        #print('yz = ',yz)
                        yx=(((700-xn)*(yz-yn))/(xz-xn))+yn
                        print(yx)
                        x_r.append(700)
                        y_r.append(yx)
                        print(x_r)
                        print(y_r)
                                        
                                        
                                
                                
                '''==============='''
                for i in range(len(x_r)):
                        if x_r[i]==700 or x_r[i]== x_r[len(x_r)-1]:
                                break
                        if y_r[i]<=y_r[i+1]:
                                S=abs(y_r[i])*(x_r[i+1]-x_r[i])+(x_r[i+1]-x_r[i])*abs(y_r[i]-y_r[i+1])/2
                        else:
                                S=abs(y_r[i+1])*(x_r[i+1]-x_r[i])+(x_r[i+1]-x_r[i])*abs(y_r[i]-y_r[i+1])/2
                
                        summ=summ+S
                print(summ)        
        red=int(summ*255/100)
        print("Красный = ",red)
        return red
        
def filter_green(X,Y):
        x_g=[]
        y_g=[]
        x=X
        y=Y
        x_min=[]
        x_max=[]
        y_min=[]
        y_max=[]
        summ=0
        for i in range(len(x)):
                if x[i]>=500 and x[i]<=600:
                      x_g.append(x[i])
                      y_g.append(y[i])
                      

        '''==============='''
        #print(y_g)
        if x_g!=[]:
                if min(x_g)!=500:
                        for i in range(len(x)):
                                if x[i]<500:
                                    x_min.append(x[i])
                                    y_min.append(y[i])
                        z=(x_min.index(max(x_min)))
                        xn=x_min[z]
                        yn=y_min[z]
                        
                        #print(max(x_min))
                        #print('index = ',z)
                        #print(yn)

                        z=x_g.index(min(x_g))
                        xz=x_g[z]
                        yz=y_g[z]
                        #print('xmax = ',xz)
                        #print('ymax = ',yz)
        
                        yx=(((500-xn)*(yz-yn))/(xz-xn))+yn
                        #print('rezult = ',y)
                 
                        x_g.insert(0,500)
                        y_g.insert(0,yx)
                        print(x_g)
                        print(y_g)
                        x_min.clear()
                        y_min.clear()

        
                '''==============='''
                        
                if max(x)>600 and max(x_g)!=600:
                        xn=max(x_g)
                        z=x_g.index(max(x_g))
                        #print("red border = ",z)
                        yn=y_g[z]
                        for i in range(len(x)):
                                if x[i] > 600 :
                                        x_min.append(x[i])
                                        y_min.append(y[i])
                        xz=min(x_min)
                        print('xz = ',xz)
                        z=x_min.index(min(x_min))
                        yz=y_min[z]
                        #print('xz = ',xz)
                        #print('yz = ',yz)
                        yx=(((600-xn)*(yz-yn))/(xz-xn))+yn
                        #print(yx)
                        x_g.append(600)
                        y_g.append(yx)
                        print(x_g)
                        print(y_g)
                
                


                
                for i in range(len(x_g)):
                        if x_g[i]==600 or x_g[i] == x_g[len(x_g)-1]:
                                break
                        if y_g[i]<=y_g[i+1]:
                                S=abs(y_g[i])*(x_g[i+1]-x_g[i])+(x_g[i+1]-x_g[i])*abs(y_g[i]-y_g[i+1])/2
                                
                        else:
                                S=abs(y_g[i+1])*(x_g[i+1]-x_g[i])+(x_g[i+1]-x_g[i])*abs(y_g[i]-y_g[i+1])/2
                
                        summ=summ+S
                print(summ)
        green=int(summ*255/100)
        print("Зеленый = ",green)
        return green
    

def filter_blue(X,Y):
        x_b=[]
        y_b=[]
        x_min=[]
        y_min=[]
        x_max=[]
        y_max=[]
        
        x=X
        y=Y
        summ=0
        
        for i in range(len(x)):
                if x[i]>=400 and x[i]<=500:
                        
                      x_b.append(x[i])
                      y_b.append(y[i])
        '''==============='''

        if x_b!=[]:
                '''==============='''
                if min(x_b)!=400 and min(x)<=400:
                        for i in range(len(x)):
                                if x[i]<400:
                                    x_min.append(x[i])
                                    y_min.append(y[i])
                        z=(x_min.index(max(x_min)))
                        xn=x_min[z]
                        yn=y_min[z]
        
                        #print(max(x_min))
                        #print('index = ',z)
                        #print(yn)

                        z=x_b.index(min(x_b))
                        xz=x_b[z]
                        yz=y_b[z]
                        #print('xmax = ',xz)
                        #print('ymax = ',yz)
        
                        yx=(((400-xn)*(yz-yn))/(xz-xn))+yn
                        #print('rezult = ',y)
                 
                        x_b.insert(0,400)
                        y_b.insert(0,yx)
                        x_min.clear()
                        y_min.clear()
                        print(x_b)
                        print(y_b)


        
                

                if max(x)>500 and max(x_b)!=500:
                        xn=max(x_b)
                        z=x_b.index(max(x_b))
                        #print("red border = ",z)
                        yn=y_b[z]
                        for i in range(len(x)):
                                if x[i] > 500 :
                                        x_min.append(x[i])
                                        y_min.append(y[i])
                        xz=min(x_min)
                        print('xz = ',xz)
                        z=x_min.index(min(x_min))
                        yz=y_min[z]
                        #print('xz = ',xz)
                        #print('yz = ',yz)
                        yx=(((500-xn)*(yz-yn))/(xz-xn))+yn
                        print(yx)
                        x_b.append(500)
                        y_b.append(yx)
                        print(x_b)
                        print(y_b)

                
        
                for i in range(len(x_b)):
                        if x_b[i]==500 or x_b[i] == x_b[len(x_b)-1]:
                                break
                        if y_b[i]<=y_b[i+1]:
                                S=abs(y_b[i])*(x_b[i+1]-x_b[i])+(x_b[i+1]-x_b[i])*abs(y_b[i]-y_b[i+1])/2
                        else:
                                S=abs(y_b[i+1])*(x_b[i+1]-x_b[i])+(x_b[i+1]-x_b[i])*abs(y_b[i]-y_b[i+1])/2
                
                        summ=summ+S
                print(summ)
        
        blue=int(summ*255/100)
        print('синий = ',blue)
        return blue

    
#x=[100,200,300,380,410,440,480,520,630,650,690]
#y=[10,20,30,0.2,0.1,0.4,0.2,0.3,0.4,0.5,0.3]
#x1=[]
#filter_red(x,y)
#filter_green(x,y)
#filter_blue(x,y)
#file_path = r'C:\Users\влад\Downloads\Координаты.txt'
#x=plot_graph_smart_1(file_path)
#print(x)
