import tkinter as tk
from tkinter import ttk

import shutil
import os

suffix=r'USER\Client\0\Profiles\default'

files=('attributes.xml','actionmaps.xml')

currentPath=os.getcwd()



class scTools():
    
    path=''
    version=''
    
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('600x250')
        self.root.title('SC Tools')
        
        
        self.mainframe=tk.Frame(self.root)
        self.mainframe.pack(fill='both',expand=True)
        
        
        
        self.title=ttk.Label(self.mainframe,text='SC Tools',font=("Brass Mono",30))
        self.title.grid(row=0,column=0)
        
        
        self.pathInput=tk.Entry(self.mainframe)
        self.pathInput.grid(row=1,column=0,pady=10,sticky='ew')
        
        pathButton=ttk.Button(self.mainframe,text='set RSI path',command=self.setPath)
        pathButton.grid(row=1,column=2,pady=10)

        pathDefaultButton=ttk.Button(self.mainframe,text='use Default path',command=self.defaultPath)
        pathDefaultButton.grid(row=1,column=3,pady=10)
        

        versions=["LIVE","PTU"]      
        self.Version=ttk.Combobox(self.mainframe,values=versions)
        self.Version.grid(row=2,column=0,pady=10,sticky='ew')
        
        versionButton=ttk.Button(self.mainframe,text='set version',command=self.setVersion) 
        versionButton.grid(row=2,column=2,pady=10)
        
        
        
        self.pathText=ttk.Label(self.mainframe,text='Path undifined')
        self.pathText.grid(row=3,column=0,pady=10)
        
        
        
        backupButton=ttk.Button(self.mainframe,text='Backup',command=self.backup)
        backupButton.grid(row=4,column=0,pady=10)
        restoreButton=ttk.Button(self.mainframe,text='Restore',command=self.restore)
        restoreButton.grid(row=4,column=1,pady=10)
        
        
        self.statusText=ttk.Label(self.mainframe,text='Status: waiting on cammand')
        self.statusText.grid(row=5,column=0,pady=10)
        
        
        self.root.mainloop()
        return
    
    def updatePathText(self):
        self.pathText.config(text=self.path+'\\'+self.version+'\\'+suffix)
        return
    
    
    def setPath(self):
        self.path=self.pathInput.get()
        self.updatePathText()
        return
    
    def setVersion(self):
        self.version=self.Version.get()
        self.updatePathText()
        return
    
    def defaultPath(self):
        self.path=r'C:\Program Files\Roberts Space Industries\StarCitizen'
        self.pathInput.delete(0,tk.END)
        self.pathInput.insert(0,self.path)
        self.updatePathText()
        return
    
    def backup(self):
        labelcount=0
        for file in files:
            if os.path.isfile(self.path+'\\'+self.version+'\\'+suffix+'\\'+file):
                shutil.copy(self.path+'\\'+self.version+'\\'+suffix+'\\'+file,os.getcwd()+'\\'+file)
                labelcount+=1
            else:
                print('file not found: '+self.path+'\\'+self.version+'\\'+suffix+'\\'+file)
        self.statusText.config(text='Status: '+str(labelcount)+' files backed up, out of '+str(len(files)))
        return
    
    def restore(self):
        labelcount=0
        for file in files:
            if os.path.isfile(currentPath+'\\'+file):
                shutil.copy(os.getcwd()+'\\'+file,self.path+'\\'+self.version+'\\'+suffix+'\\'+file)
                labelcount+=1
            else:
                print('file not found: '+os.getcwd()+'\\'+file)
        self.statusText.config(text='Status: '+str(labelcount)+' files restored, out of '+str(len(files)))
        return
    
    

    

if __name__ == '__main__':
    scTools()