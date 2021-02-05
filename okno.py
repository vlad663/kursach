from PyQt5 import QtWidgets,QtCore
from ui_MyForm2 import Ui_Form
from poptka_2 import data_read,filter_red,filter_green,filter_blue
from matplotlib import pyplot as plt
from  matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from MplForWidget import MyMplCanavas

class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__ (self,parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.knopka)
        self.pushButton_2.clicked.connect(self.knopka2)

        self.fig,self.axes=plt.subplots(nrows=1,ncols=1,figsize=(4,4))    
        self.axes.grid(True,c='lightgrey',alpha=0.5)
        self.axes.set_title('spectr')
        x=[400,400] #красный
        y=[0,1]
        x2=[500,500] # переходный красный-зеленый
        x3=[600,600] # Переходный зеленый-синий
        x4=[700,700] # Синий

        self.axes.plot(x,y,color='blue')
        self.axes.plot(x2,y,color='green')
        self.axes.plot(x3,y,color='green')
        self.axes.plot(x4,y,color='red')
        self.companovka_for_mpl = QtWidgets.QVBoxLayout(self.widget)
        self.canavas=MyMplCanavas(self.fig)
        self.companovka_for_mpl.addWidget(self.canavas)
        self.toolbar=NavigationToolbar(self.canavas,self)
        self.companovka_for_mpl.addWidget(self.toolbar)
        self.Text.setPlainText("The program is ready to work. Please open the file containing the spectrum.")

    def knopka(self):
        
        file=QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                  caption = "Выбирете текстовый файл",
                                                  filter = "Текстовый файл (*.txt)")
        print(file[0])
        status=data_read(file[0])

        '''============='''
        self.x=status[0]
        self.y=status[1]
        self.tableWidget.setRowCount(len(self.x)) 

        self.i=0    #для прохода по левой колонке 
        self.ii=0     # для прохода по массиву
        self.iii=1   # для прохода по правой колонке
        print('self.x =',self.x)
        print('self.y =',self.y)
        for i in range(len(self.x)):
                       self.tablica(self.x,self.y)


        '''================'''
        if(status!=[[],[]]):
              
            self.axes.plot(status[0],status[1])
            self.fig.canvas.draw()
            self.Text.clear()
            self.Text.setPlainText("Data uploaded successfully")
            self.tableWidget.setRowCount(len(status[0]))
            r1=filter_red(status[0],status[1])
            g1=filter_green(status[0],status[1])
            b1=filter_blue(status[0],status[1])
            
            
            
            #чисто эксперемент  но рабочий!!!               
            r=str(r1)
            g=str(g1)
            b=str(b1)
            
            self.widget_2.setStyleSheet("background-color:rgb("+r+','+g+','+b+";)")
            
        else:
            self.Text.clear()
            self.Text.setPlainText("Something went wrong.Check the file for errors.")
        self.pushButton.setEnabled(False)
        
    def knopka2(self):
        #self.Text.setPlainText("Something went wrong")
        self.widget_2.setStyleSheet("background-color:white")
        self.axes.clear()
        self.axes.grid(True,c='lightgrey',alpha=0.5)
        self.axes.set_title('spectr')
        x=[400,400] #красный
        y=[0,1]
        x2=[500,500] # переходный красный-зеленый
        x3=[600,600] # Переходный зеленый-синий
        x4=[700,700] # Синий

        self.axes.plot(x,y,color='blue')
        self.axes.plot(x2,y,color='green')
        self.axes.plot(x3,y,color='green')
        self.axes.plot(x4,y,color='red')
        self.fig.canvas.draw()
        self.pushButton.setEnabled(True)
        self.Text.setPlainText("Data cleared successfully")
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels([" X ", " Y "])
        self.tableWidget.setRowCount(10) 
        
    def tablica(self,x,y): 
        l=self.x[self.ii]
        l1=str(l)
        r=self.y[self.ii]
        r1=str(round(r,7))
        c=QtWidgets.QTableWidgetItem (l1)
        c.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0,self.i,c)
        
        c2=QtWidgets.QTableWidgetItem (r1)
        c2.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0,self.iii,c2)
        self.i=self.i+2
        self.ii=self.ii+1
        self.iii=self.iii+2






        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    #file_path = r'C:\Users\влад\Downloads\Координаты.txt'
