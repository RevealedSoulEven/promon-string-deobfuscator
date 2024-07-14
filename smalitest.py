import re


smali = []
with open("CryptLib.smali") as f:
    for i in f.readlines():
        i_ = i.replace("\n", "")
        if len(i_.split()) > 0:
            smali.append(i_.strip())


array_declared = False
arrayname = ""

cmds = []


def combine(source):
    cmd1 = cmds[-2]
    cmd2 = cmds[-1]
    cmds.pop()
    cmds.pop()
    ele__ = cmd2.split(" ")[0]
    dat__ = cmd1.split(" = ")[1]
    
    if source == "int-to-char":
        cmds.append(f"{ele__} = chr({dat__})")    
    if source == "aput-char":
        cmds.append(f"{ele__} = ({dat__})")
        


for index in range(len(smali)):
    line = smali[index]
    op__ = line.split(" ")
    
    if "new-array" in line and "[C" in line:
        arraysize__ = op__[2].replace(",",'')
        arrayname = op__[1].replace(",","")
        
        ##### get size
        if "const/" in smali[index-1]:
            op__2 = smali[index-1].split(" ")
            arraysize = int(op__2[2], 16)
            cmds.append(f"{arrayname} = [None] * {arraysize}")
            array_declared = True
    
          
    if array_declared:
        
        if "xor-int/lit16" in line:
            out__ = op__[1].replace(",","")
            to_be_added = op__[2].replace(",","")
            opval__ = op__[3]
            
            if "const" in smali[index-1]:
                op__2 = smali[index-1].split(" ")
                op2val__ = op__2[2]
                if op__2[1].replace(",",'') == to_be_added:
                    cmds.append(f"{out__} = {op2val__} ^ {opval__}")
            elif "aget-char" in smali[index-1]:
                op__2 = smali[index-1].split(" ")
                temp__ = cmds[-1]
                cmds.pop()
                op__temp = temp__.split(" ")
                if op__2[1].replace(",",'') == to_be_added:
                    xcc = temp__.split(" = ")[1]
                    cmds.append(f"{out__} = ord({xcc}) ^ {opval__}")
                
                    
                    
        if "int-to-char" in line:
            cmds.append(f"{op__[1].replace(',','')} = chr({op__[2]})")
            
            combine("int-to-char")
        
        
        
        if "aput-char" in line:
            ele__ = op__[1].replace(",","")
            arr__ = op__[2].replace(",","")
            index__ = op__[3]
            
            if "const" in smali[index-1]:
                op__2 = smali[index-1].split(" ")
                if op__2[1].replace(",",'') == index__:
                    cmds.append(f"{arr__}[{int(op__2[2], 16)}] = {ele__}")
                    
                    combine("aput-char")
        
        
        if "aget-char" in line:
            ele__ = op__[1].replace(",","")
            arr__ = op__[2].replace(",","")
            index__ = op__[3]
            
            if "const" in smali[index-1]:
                op__2 = smali[index-1].split(" ")
                if op__2[1].replace(",",'') == index__:
                    cmds.append(f"{ele__} = {arr__}[{int(op__2[2], 16)}]")
                    
                    
                    
        
        
        if "Ljava/lang/String;->intern()" in line:
            #### close everypthing
            cmds.append(f"result_str = ''.join({arrayname})")
            cmds.append("""print("'" + result_str + "'")""")
            
            _______ = ""
            for i in cmds:
                _______ += i + "\n"
            exec(_______)
            
            cmds = []
            
            array_declared = False
            arrayname = ""
            
            
       