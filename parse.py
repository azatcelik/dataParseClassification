import os
import shutil

def dataParse(source,destination,rt=0.8):
    clss = os.listdir(source)
    ststr=0
    ststs=0
    for dst in os.listdir(destination):
        if dst=='train':
            ststr=1
        elif dst=='test':
            ststs=1
        if ststs==0:
            os.mkdir(destination+"/test")
        elif ststr==0:
            os.mkdir(destination+"/train")
    for cls in clss:
        cn=os.listdir(source+"/"+cls)
        trn=(len(cn))*rt
        train=cn[:int(trn)]
        test=cn[int(trn):]
        os.mkdir(destination+"/train/"+cls)
        os.mkdir(destination+"/test/"+cls)
        for tr in train:
            shutil.copy(source+"/"+cls+"/"+tr,destination+"/train/"+cls+"/"+tr)
        for ts in test:
            shutil.copy(source+"/"+cls+"/"+ts,destination+"/test/"+cls+"/"+ts)