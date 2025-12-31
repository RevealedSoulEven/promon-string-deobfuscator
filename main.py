import os
import json
import shutil
from tqdm import tqdm
from colorama import Fore, Style, init

import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed


init(autoreset=True)
array_declared = False
arrayname = ""
cmds = []
method_name = ""
method_para = ""
curr_class = ""
available_methods = []



def get_temp_file():
    return f"tempsouleven_{os.getpid()}.py"

def methodify(st):
    if "->" in st:
        ## method
        owch = st.split(";->")
        _oO_ = f"{owch[0].replace('/','_')}_{owch[1].replace('(I)[C','')}"
    else:
        _oO_ = st.replace("/","_").replace(";","")
        _oO_ = _oO_.replace("$","tempsoul")
    return _oO_
    
    
def demethodify(st):
    return st.replace('_','/').replace('tempsoul','$')


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
                    
                    # print(new_string_)    # to check whether it is getting decrypted strings or not
                    
                    
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
    
    
    called_method = None
    for line in smali:
        if "invoke-" in line and "(I)[C" in line:
            called_method = methodify(line.split()[-1])
            break
        
    
    if called_method and os.path.exists(get_temp_file()):
        with open(get_temp_file()) as f:
            method_code = []
            in_target_method = False
            for line in f.readlines():
                if line.startswith(f"def {called_method}("):
                    in_target_method = True
                    method_code.append(line)
                elif in_target_method:
                    if line.startswith("def "):
                        # Reached next method or empty line (end of current method)
                        break
                    method_code.append(line)
            cmds.extend(method_code)
    

    for index in range(len(smali)):
        line = smali[index]
        op__ = line.split(" ")
        # specific is_method_call opcodes
        
        if "const " in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2]}")
                
        if "sub-int" in line:
            if "rsub" in line:
                cmds.append(f"{op__[1].replace(',','')} = {op__[3]} - {op__[2].replace(',','')}")
            else:
                cmds.append(f"{op__[1].replace(',','')} = {op__[2].replace(',','')} - {op__[3]}")
                
        if "add-int" in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2].replace(',','')} + {op__[3]}")
            
        if "xor-int" in line:
            cmds.append(f"{op__[1].replace(',','')} = {op__[2].replace(',','')} ^ {op__[3]}")
            
        if demethodify(curr_class) in line:
            #got calling method
            last_var_ = cmds[-1].split(" ")[2]
            method__ = methodify(line.split(" ")[-1])
            cmds.append(f"result_str = {method__}({last_var_})")
            
        
    _______ = ""
    for i in cmds:
       _______ += i + "\n"
        
    cmds = []
    with open("temp.py","w") as f:
        f.write(_______)
    ret__ = {}
    exec(_______, globals(), ret__)
            
    new_string_ = ret__["result_str"]
    
    java_friendly_string = json.dumps(new_string_)
    java_friendly_string = java_friendly_string[1:-1]
    new_string_ = java_friendly_string
       
    os.remove("temp.py")
       
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
                with open(get_temp_file(),"w") as f:
                    f.write("")

            if all(op_op not in line for op_op in method_ops_):
                found__, is_method, start_line, end_line = False, False, -1, -1
                # print(f"----------x---------------------{line}")

            elif "return-object" in line:
                try:
                    end_line = curr_line + 1
                    method_cmds = deobfuscate(curr_smali[start_line:end_line], True)
                    with open(get_temp_file(),"a") as f:
                        f.write(method_cmds)
                    found__, is_method, start_line, end_line = False, False, -1, -1
                except:
                    found__, is_method, start_line, end_line = False, False, -1, -1

    
    found__, is_method, start_line, end_line, curr_line = False, False, -1, -1, -1
    for line in curr_smali:
        curr_line += 1
        
        my_ops_ = [
            ".line", "const", "xor-int/lit16", "int-to-char",
            "aput-char", "aget-char", " Ljava/lang/String", "const/16"
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
                "aput-char", "aget-char", " Ljava/lang/String",
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
                    try:
                        new_lines = deobfuscate_method(curr_smali[start_line:end_line])
                        changes.append((start_line, end_line, new_lines))
                    except:
                        pass
                    found__, is_method, start_line, end_line = False, False, -1, -1
                    found__confirm = False

                if ".line" in line:
                    start_line = curr_line
                    found__ = True

    changes = sorted(changes, key=lambda x: x[0])
    for start_line, end_line, new_lines in reversed(changes):
        curr_smali[start_line:end_line] = new_lines

    if is_temp_written:
        os.remove(get_temp_file())
    available_methods = []
    return curr_smali, None






def _worker(args):
    input_filepath, folder, folderout = args

    relative_path = os.path.relpath(input_filepath, folder)
    output_filepath = os.path.join(folderout, relative_path)

    if os.path.exists(output_filepath):
        return None

    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    new_lines, error = process_file(input_filepath)

    if error:
        shutil.copyfile(input_filepath, output_filepath)
        return f"copied: {relative_path}"

    if new_lines:
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))

    return relative_path


def process_folder(folder, folderout):
    all_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".smali"):
                all_files.append(os.path.join(root, file))

    os.makedirs(folderout, exist_ok=True)

    cpu_count = multiprocessing.cpu_count()
    print(f"[+] Using {cpu_count} CPU cores")

    tasks = [(fp, folder, folderout) for fp in all_files]

    with ProcessPoolExecutor(max_workers=cpu_count) as executor:
        futures = [executor.submit(_worker, task) for task in tasks]

        with tqdm(
            total=len(futures),
            desc=Fore.CYAN + "Decrypting smali",
            unit="file",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"
        ) as pbar:
            for future in as_completed(futures):
                _ = future.result()
                pbar.update(1)


def banner():
    print(Fore.CYAN + Style.BRIGHT + """

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
    """ + Style.RESET_ALL)

    print(
        Fore.MAGENTA + Style.BRIGHT +
        "        ▓▒░  Promon Shield String Deobfuscator Tool  ░▒▓\n" +
        Style.RESET_ALL
    )




import argparse
import subprocess
import glob

def find_jar(prefix):
    jars = glob.glob(f"{prefix}*.jar")
    if not jars:
        raise FileNotFoundError(f"{prefix}*.jar not found")
    return jars[0]

APKTOOL_JAR = find_jar("apktool")

def run(cmd, cwd=None, title=None):
    if title:
        print(Fore.GREEN + Style.BRIGHT + f"\n[+] {title}\n")

    p = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in p.stdout:
        if line.startswith("I:"):
            print(Fore.BLACK + Style.BRIGHT + line.strip())
        elif line.startswith("W:"):
            print(Fore.YELLOW + line.strip())
        elif line.startswith("E:"):
            print(Fore.RED + line.strip())
        else:
            print(Fore.WHITE + line.strip())

    p.wait()
    if p.returncode != 0:
        raise subprocess.CalledProcessError(p.returncode, cmd)

def decrypt_apk(apk_path, out_apk):
    apk_path = os.path.abspath(apk_path)
    base = os.getcwd()
    workdir = os.path.join(base, "apktool_work")
    decoded = os.path.join(workdir, "decoded")

    if os.path.exists(workdir):
        print(Fore.YELLOW + "[*] Removing old apktool_work folder")
        shutil.rmtree(workdir)

    os.makedirs(workdir, exist_ok=True)

    run(
        ["java", "-jar", APKTOOL_JAR, "d", "-f", apk_path, "-o", decoded],
        title="Decompiling APK"
    )

    smali_dirs = [
        d for d in os.listdir(decoded)
        if d == "smali" or d.startswith("smali_classes")
    ]

    print(Fore.CYAN + f"\n[+] Found {len(smali_dirs)} smali folders\n")

    for sdir in smali_dirs:
        src = os.path.join(decoded, sdir)
        tmp = src + "_dec"

        print(Fore.YELLOW + f"\n[*] Decrypting {sdir}")
        process_folder(src, tmp)

        shutil.rmtree(src)
        os.rename(tmp, src)

    run(
        ["java", "-jar", APKTOOL_JAR, "b", decoded, "-o", out_apk],
        title="Rebuilding APK"
    )

    print(Fore.GREEN + Style.BRIGHT + f"\n[✓] Output APK: {out_apk}")





def main():
    banner()

    p = argparse.ArgumentParser()
    p.add_argument("-a", "--apk", required=True)
    p.add_argument("-o", "--out", required=True)
    args = p.parse_args()

    decrypt_apk(args.apk, args.out)


if __name__ == "__main__":
    main()