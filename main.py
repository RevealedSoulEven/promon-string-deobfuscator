import os
import json

array_declared = False
arrayname = ""
cmds = []
method_name = ""
method_para = ""
curr_class = ""
available_methods = []


def methodify(st):
    if "->" in st:
        ## method
        owch = st.split(";->")
        return f"{owch[0].replace('/','_')}_{owch[1].replace('(I)[C','')}"
    return st.replace("/","_").replace(";","")
    
    
def demethodify(st):
    return st.replace('_','/')


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
        

def deobfuscate(smali, is_method):
    global array_declared, arrayname, cmds, method_name, method_para, available_methods, curr_class
    
    for index in range(len(smali)):
        line = smali[index]
        op__ = line.split(" ")
        
        if is_method and ".method" in line:
            method_name = line.split(" ")[-1].replace("(I)[C","")
        
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
                
                          
            if "xor-int " in line:     #xor-int only come in methods
                out__ = op__[1].replace(",","")
                to_be_added = op__[2].replace(",","")
                opval__ = op__[3]
                method_para = op__[3]
            
                if "const" in smali[index-1]:
                    op__2 = smali[index-1].split(" ")
                    op2val__ = op__2[2]
                    if op__2[1].replace(",",'') == to_be_added:
                        cmds.append(f"{out__} = {op2val__} ^ {opval__}")
                        
                        
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
                        
            # only in case of is_method return the python code       
            if "return-object" in line and is_method:
                if len(cmds) > arraysize:
                    #### close everypthing
                    cmds.append(f"result_str = ''.join({arrayname})")
                    cmds.append(f"return result_str")
                    
                    c_m_d = []
                    c_m_d.append(f"def {curr_class}_{method_name}({method_para}):")
                    available_methods.append(f"{curr_class}_{method_name}")
                    for i in cmds:
                        if "(chr(" in i:
                            _o_ = i.replace("(chr(", "(chr((").replace("))", ") & 0xFFFF))")
                            c_m_d.append(_o_)
                        else:
                            c_m_d.append(i)
                    
                            
                    cmds = []     
                    array_declared = False
                    arrayname = ""
                    
                    _______ = ""
                    for i in c_m_d:
                        if "def " in i:
                            _______ += "\n\n" + i + "\n"
                        else:
                            _______ +="    " + i + "\n"
                    
                    return _______   
            
            
            if "Ljava/lang/String;->intern()" in line:
                if len(cmds) > arraysize:
                    #### close everypthing
                    cmds.append(f"result_str = ''.join({arrayname})")
                    # cmds.append("""print("'" + result_str + "'")""")
                    
                    #### fixing the chr() range (req for java to python)
                    c_m_d = []
                    for i in cmds:
                        if "(chr(" in i:
                            _o_ = i.replace("(chr(", "(chr((").replace("))", ") & 0x10FFFF))")
                            c_m_d.append(_o_)
                        else:
                            c_m_d.append(i)
                            
                    
                    cmds = []     
                    array_declared = False
                    arrayname = ""
                    
                    _______ = ""
                    for i in c_m_d:
                        _______ += i + "\n"

                    ret__ = {}
                    exec(_______, globals(), ret__)
                    

                    new_string_ = ret__["result_str"]
                    java_friendly_string = json.dumps(new_string_)
                    java_friendly_string = java_friendly_string[1:-1]
                    new_string_ = java_friendly_string
                else:
                    return smali
            
    try:
        new_lines = []
        start___, end___ = False, False
        for line in smali:
            if not start___ and "new-array" in line and "[C" in line:
                new_lines.pop() # removes the previous declared size of the array as const
                start___ = True
            elif start___ and not end___ and "Ljava/lang/String;->intern()" in line:
                end___ = True
            elif end___ and start___:
                # get move-result-object v0
                if line.split()[0] == "move-result-object":
                    var_ = line.split()[1]
                    new_lines.append(f'''const-string {var_}, "{new_string_}"''')
                    end___, start___ = False, False
            elif not start___ and not end___:
                new_lines.append(line)
                
    except:
        new_lines = smali
    
    return new_lines
                                       
                
def deobfuscate_method(smali):
    global array_declared, arrayname, cmds, method_name, method_para, available_methods, curr_class
    
    cmds.append("import tempsouleven")
    
    for index in range(len(smali)):
        line = smali[index]
        op__ = line.split(" ")
        # specific is_method_call opcodes
        
        if "const " in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2]}")
                
        if "sub-int" in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2].replace(',','')} - {op__[3]}")
                
        if "add-int" in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2].replace(',','')} + {op__[3]}")
            
        if "xor-int" in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2].replace(',','')} ^ {op__[3]}")
            
        if demethodify(curr_class) in line:
            #got calling method
            last_var_ = cmds[-1].split(" ")[2]
            method__ = methodify(line.split(" ")[-1])
            cmds.append(f"result_str = tempsouleven.{method__}({last_var_})")
            
        
    _______ = ""
    for i in cmds:
       _______ += i + "\n"
        
    cmds = []
        
    ret__ = {}
    exec(_______, globals(), ret__)
            
    new_string_ = ret__["result_str"]
    java_friendly_string = json.dumps(new_string_)
    java_friendly_string = java_friendly_string[1:-1]
    new_string_ = java_friendly_string
       
       
    try:
        new_lines = []
        start___, end___ = False, False
        for line in smali:
            if not start___ and ".line" in line:
                start___ = True
            elif start___ and not end___ and "Ljava/lang/String;->intern()" in line:
                end___ = True
            elif end___ and start___:
                # get move-result-object v0
                if line.split()[0] == "move-result-object":
                    var_ = line.split()[1]
                    new_lines.append(f'''const-string {var_}, "{new_string_}"''')
                    end___, start___ = False, False
            elif not start___ and not end___:
                new_lines.append(line)
                
    except:
        new_lines = smali
    
    return new_lines
     
            


########################## file handling #############################
######################## analysing toooooooo #########################

def process_file(filepath):
    global available_methods, curr_class
    
    curr_smali = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                if len(line.split()) > 0:
                    curr_smali.append(line.strip())
    except (UnicodeDecodeError, IOError) as e:
        return None, e
    
    found__ = False
    start_line = -1
    curr_line = -1
    changes = []
    is_method = False
    is_temp_written = False
    
    
    #### as the char[] methods are randomly distributed,
    #### why not first search and keep the method?,
    

    for line in curr_smali:
        curr_line += 1
        
        method_ops_ = [
            ".line", "const", "xor-int/lit16", "int-to-char",
            "aput-char", "aget-char", "return-object", "const/16",
            "xor-int"    ## for methods
        ]
        
        if ".class" in line:
            curr_class = methodify(line.split()[-1])
        
        if not found__:
            if line.startswith(".method") and line.endswith("(I)[C"):
                is_method = True
            
            # respresents that method char has ended without interaction of new-array
            if ".end method" in line and is_method:
                is_method = False
            
            if "new-array" in line and "[C" in line and is_method:
                start_line = (curr_line - 5) if (curr_line - 5) >= 0 else 0
                found__ = True
        else:
            # if is_method

            if not is_temp_written:
                is_temp_written = True
                with open("tempsouleven.py","w") as f:
                    f.write("")

            if all(op_op not in line for op_op in method_ops_):
                found__, is_method, start_line, end_line = False, False, -1, -1
                print(f"----------x---------------------{line}")

            elif "return-object" in line:
                try:
                    end_line = curr_line + 1
                    method_cmds = deobfuscate(curr_smali[start_line:end_line], True)
                    with open("tempsouleven.py","a") as f:
                        f.write(method_cmds)
                    found__, is_method, start_line, end_line = False, False, -1, -1
                except:
                    found__, is_method, start_line, end_line = False, False, -1, -1

    
    found__, is_method, start_line, end_line, curr_line = False, False, -1, -1, -1
    for line in curr_smali:
        curr_line += 1
        
        my_ops_ = [
            ".line", "const", "xor-int/lit16", "int-to-char",
            "aput-char", "aget-char", "Ljava/lang/String", "const/16"
        ]
        
        if not found__:
            
            if "new-array" in line and "[C" in line:
                start_line = (curr_line - 5) if (curr_line - 5) >= 0 else 0
                found__ = True

        # skipping if found other opcodes so it may skip some but, who cares?
        
        else:
            if all(op_op not in line for op_op in my_ops_) or ".end method" in line:
                found__, is_method, start_line, end_line = False, False, -1, -1
                #print(f"--------------------------------{line}")
        
            elif "Ljava/lang/String;->intern()" in line:
                end_line = curr_line + 2
                new_lines = deobfuscate(curr_smali[start_line:end_line], False)
                changes.append((start_line, end_line, new_lines))
                found__, is_method, start_line, end_line = False, False, -1, -1
                
    
    found__, is_method, start_line, end_line, curr_line = False, False, -1, -1, -1
    ## finally last loop for methods
    found__confirm = False
    if is_temp_written:
        ## means methods exist
        for line in curr_smali:
            curr_line += 1

            my_ops_ = [
                "const", "xor-int", "int-to-char",
                "aput-char", "aget-char", "Ljava/lang/String",
                "sub-int", "add-int", "invoke-", "move-"
            ]
            
            if not found__:
                 #sorry but I got no better way to get the beginning of method calls
                 #all of them begin with .line only hhehe
                if ".line" in line:
                    start_line = curr_line
                    found__ = True

            else:

                if all(op_op not in line for op_op in my_ops_) or ".end method" in line:
                    found__, is_method, start_line, end_line = False, False, -1, -1
                    #print(f"--------------------------------{line}")

                elif "invoke-" in line and "(I)[C" in line:
                    found__ = True
                    found__confirm = True # specially for method cases
                    if methodify(line.split()[-1]) not in available_methods:
                        found__, is_method, start_line, end_line = False, False, -1, -1
                        found__confirm = False

                elif "Ljava/lang/String;->intern()" in line and found__confirm:
                    end_line = curr_line + 2               
                    new_lines = deobfuscate_method(curr_smali[start_line:end_line])
                    changes.append((start_line, end_line, new_lines))
                    found__, is_method, start_line, end_line = False, False, -1, -1
                    found__confirm = False

                if ".line" in line:
                    start_line = curr_line
                    found__ = True

    changes = sorted(changes, key=lambda x: x[0])
    for start_line, end_line, new_lines in reversed(changes):
        curr_smali[start_line:end_line] = new_lines

    if is_temp_written:
        os.remove("tempsouleven.py")
    available_methods = []
    return curr_smali, None








def process_folder(folder, folderout):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".smali"):
                input_filepath = os.path.join(root, file)
                
                relative_path = os.path.relpath(input_filepath, folder)
                output_filepath = os.path.join(folderout, relative_path)
                if os.path.exists(output_filepath):
                    print(f"File {output_filepath} already exists. Skipping.")
                else:
                    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                    
                    new_lines, error = process_file(input_filepath)
                    
                    if error:
                        # Copy the original file to the output directory
                        shutil.copyfile(input_filepath, output_filepath)
                        print(f"Error processing {input_filepath}: {error}. Copied original file.")
                    elif new_lines:
                        # Write the modified lines to the output file
                        with open(output_filepath, "w", encoding="utf-8") as f:
                            for line in new_lines:
                                f.write(line + "\n")
                        print(f"Wrote : {output_filepath}")

# Example usage
folder = "classes"
folderout = "classes_dec"
process_folder(folder, folderout)



































print("""

██████╗░███████╗██╗░░░██╗███████╗░█████╗░██╗░░░░░███████╗██████╗░
██╔══██╗██╔════╝██║░░░██║██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗
██████╔╝█████╗░░╚██╗░██╔╝█████╗░░███████║██║░░░░░█████╗░░██║░░██║
██╔══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██║██║░░░░░██╔══╝░░██║░░██║
██║░░██║███████╗░░╚██╔╝░░███████╗██║░░██║███████╗███████╗██████╔╝
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░

░██████╗░█████╗░██╗░░░██╗██╗░░░░░███████╗██╗░░░██╗███████╗███╗░░██╗
██╔════╝██╔══██╗██║░░░██║██║░░░░░██╔════╝██║░░░██║██╔════╝████╗░██║
╚█████╗░██║░░██║██║░░░██║██║░░░░░█████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║
░╚═══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║
██████╔╝╚█████╔╝╚██████╔╝███████╗███████╗░░╚██╔╝░░███████╗██║░╚███║
╚═════╝░░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝

""")

