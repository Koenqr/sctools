import tkinter as tk
from tkinter import ttk

import shutil
import os

suffix=r'USER\Client\0\Profiles\default'

files=('attributes.xml','actionmaps.xml')
cfgFile='USER.cfg'

currentPath=os.getcwd()



class scTools():
    
    path=''
    version=''
    
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('600x280')
        self.root.title('SC Tools')
        
        noteBook=ttk.Notebook(self.root)
        noteBook.pack(expand=True,fill='both')
        
        self.settingsFrame=ttk.Frame(noteBook)
        self.settingsFrame.pack(fill='both',expand=True)
        
        
        self.title=ttk.Label(self.settingsFrame,text='SC Tools',font=("Brass Mono",30))
        self.title.grid(row=0,column=0)
        
        
        self.pathInput=tk.Entry(self.settingsFrame)
        self.pathInput.grid(row=1,column=0,pady=10,sticky='ew')
        
        pathButton=ttk.Button(self.settingsFrame,text='set RSI path',command=self.setPath)
        pathButton.grid(row=1,column=2,pady=10)

        pathDefaultButton=ttk.Button(self.settingsFrame,text='use Default path',command=self.defaultPath)
        pathDefaultButton.grid(row=1,column=3,pady=10)
        

        versions=["LIVE","PTU","EPTU"]      
        self.Version=ttk.Combobox(self.settingsFrame,values=versions)
        self.Version.grid(row=2,column=0,pady=10,sticky='ew')
        
        versionButton=ttk.Button(self.settingsFrame,text='set version',command=self.setVersion) 
        versionButton.grid(row=2,column=2,pady=10)
        
        
        
        self.pathText=ttk.Label(self.settingsFrame,text='Path undifined')
        self.pathText.grid(row=3,column=0,pady=10)
        
        
        
        backupButton=ttk.Button(self.settingsFrame,text='Backup',command=self.backup)
        backupButton.grid(row=4,column=0,pady=10)
        restoreButton=ttk.Button(self.settingsFrame,text='Restore',command=self.restore)
        restoreButton.grid(row=4,column=1,pady=10)
        
        shaderButton=ttk.Button(self.settingsFrame,text='Clear Shaders',command=self.clearShaders)
        shaderButton.grid(row=4,column=2,pady=10)
        
        
        self.statusText=ttk.Label(self.settingsFrame,text='Status: waiting on cammand')
        self.statusText.grid(row=5,column=0,pady=10)
        
        
        self.cfgFrame=ttk.Frame(noteBook)
        self.cfgFrame.pack(fill='both',expand=True)
        
        
        cfgBackupButton=ttk.Button(self.cfgFrame,text='Backup',command=self.cfgBackup)
        cfgBackupButton.grid(row=0,column=0,pady=10)
        cfgRestoreButton=ttk.Button(self.cfgFrame,text='Restore',command=self.cfgRestore)
        cfgRestoreButton.grid(row=0,column=1,pady=10)
        
        
        noteBook.add(self.settingsFrame,text='Settings')
        noteBook.add(self.cfgFrame,text='cfg')
        
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
    
    def clearShaders(self):
        #remove all directories in the shader cache folder except Crashes
        #"%localappdata%\Star Citizen"
        f=os.getenv('localappdata')+'\\Star Citizen'
        foldercontent=os.listdir(f)
        for folder in foldercontent:
            if folder!='Crashes':
                shutil.rmtree(f+'\\'+folder)
        self.statusText.config(text='Status: Shaders cleared')
        return
    
    
    
    def cfgBackup(self):
        if os.path.isfile(self.path+'\\'+self.version+'\\'+cfgFile):
            shutil.copy(self.path+'\\'+self.version+'\\'+cfgFile,os.getcwd()+'\\'+cfgFile)
        else:
            print("no file found")

            
    def cfgRestore(self):
        if os.path.isfile(currentPath+'\\'+cfgFile):
            shutil.copy(os.getcwd()+'\\'+cfgFile,self.path+'\\'+self.version+'\\'+cfgFile)
        else:
            print("no file found, making new one")
            open(self.path+'\\'+self.version+'\\'+cfgFile,'w')

    
    

    

if __name__ == '__main__':
    scTools()