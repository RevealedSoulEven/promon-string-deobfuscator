import re
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

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
        

def deobfuscate(smali):
    global array_declared, arrayname, cmds
    try:
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
                    # cmds.append("""print("'" + result_str + "'")""")
                    
                    _______ = ""
                    for i in cmds:
                        _______ += i + "\n"

                    ret__ = {}
                    exec(_______, globals(), ret__)
                    
                    cmds = []     
                    array_declared = False
                    arrayname = ""

                    new_string_ = ret__["result_str"]
    except:
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
        
    # print("----------------------------------------------------------------")
    # for i in smali:
    #     print(i)
    # print("----------------------------------------------------------------")
    
    # print("\n\n\n\n\n\n")
    # print("----------------------------------------------------------------")
    # for i in new_lines:
    #     print(i)
    # print("----------------------------------------------------------------")
    
    return new_lines
                                       
                
            
            
            

def process_file(filepath):
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

    for line in curr_smali:
        curr_line += 1
        if not found__:
            if "new-array" in line and "[C" in line:
                start_line = (curr_line - 3) if (curr_line - 3) >= 0 else 0
                found__ = True
        
        elif "Ljava/lang/String;->intern()" in line:
            end_line = curr_line + 2
            new_lines = deobfuscate(curr_smali[start_line:end_line])
            changes.append((start_line, end_line, new_lines))
            found__, start_line, end_line = False, -1, -1

        elif ".end method" in line and found__:
            found__ = False
            start_line = -1

    for start_line, end_line, new_lines in reversed(changes):
        curr_smali[start_line:end_line] = new_lines

    return curr_smali, None

def process_file_wrapper(input_filepath, output_filepath):
    if os.path.exists(output_filepath):
        print(f"File {output_filepath} already exists. Skipping.")
        return
    
    new_lines, error = process_file(input_filepath)
    
    if error:
        # Copy the original file to the output directory
        shutil.copyfile(input_filepath, output_filepath)
        print(f"Error processing {input_filepath}: {error}. Copied original file.")
    else:
        # Write the modified lines to the output file
        with open(output_filepath, "w", encoding="utf-8") as f:
            for line in new_lines:
                f.write(line + "\n")
        print(f"wrote: {output_filepath}")

def process_folder(folder, folderout, max_workers=50):
    tasks = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".smali"):
                    input_filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(input_filepath, folder)
                    output_filepath = os.path.join(folderout, relative_path)
                    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                    
                    # Submit the file processing task to the executor
                    tasks.append(executor.submit(process_file_wrapper, input_filepath, output_filepath))
        
        # Wait for all tasks to complete
        for future in as_completed(tasks):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing a file: {e}")
                    

# Example usage
folder = "smali3"
folderout = "smali22"
process_folder(folder, folderout)

