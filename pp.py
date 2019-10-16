import os
import numpy as np

def Mkdir(path):
    path = path.strip()
    is_exists = os.path.isdir(path)
    if not is_exists:
        os.makedirs(path)
        print("Creation directory successful: ",path)
        return True
    else:
        print("Creation directory failure: ",path, " is exists")
        return False
#def Mkfile(path):





print("              C/CPP PROJECT CREATE\n")
print(" Current working directory: ",os.getcwd())
print(" Now Create a C/CPP project with CMake")
print(" tools: python3              Designed by whosecube\n")




is_new_project = False
while True:
    real_path = os.path.dirname(os.path.realpath(__file__))
    cmd_string = input("cmd >> ") 
    cmd_string = cmd_string.strip()
    #得到py所在的目录
    
    #create the project
    if cmd_string == "np" or cmd_string == "new project":
        project_path = input("please input the project path\n---------------\nnew project >> ") 
        build_path = project_path + "/build"
        include_path = project_path + "/include"
        src_path = project_path + "/src"
        is_new_project = True
        print("*** The project_path is '"+ project_path+"' ***")
        if Mkdir(project_path) == True:
#all directory
            Mkdir(build_path)
            Mkdir(include_path)
            Mkdir(src_path)    
            print("Creation Finished: all directorys is created")
#main.cpp
            file_main = open(project_path+"/src/main.cpp", "w", encoding = "utf-8")
            file_main.write("#include<iostream>\n\n")
            file_main.write("using namespace std;\n\n")
            file_main.write("int main()\n")
            file_main.write("{\n\n\n\n")
            file_main.write("    return 0;\n")
            file_main.write("}\n")
            file_main.close()
            print("Creation file successful: main.cpp")
#CMakeLists.txt
            os.popen("cp " +real_path+"/CMakeLists.txt " +project_path+"/CMakeLists.txt")
            print("Creation file successful: CMakeLists.txt")
#YouCompleteMe config
            os.popen("cp " +real_path+"/ycm_extra_conf.py " +project_path+"/.ycm_extra_conf.py")
            print("Creation file successful: ycm_extra_conf.py")
#README
            file_readme = open(project_path+"/README.md", "w", encoding = "utf-8")
            file_readme.close()
            print("Creation file successful: README.md")
            print("Create Finish: all files is created")

    elif cmd_string == "nc" or cmd_string == "new class":
        if is_new_project == True:
            class_string = input("Please input the class name\n---------------\nnew class >> ")
            class_list = class_string.split()
            success_class = 0
            print("Target: ", len(class_list), " classes")
            for i in range(0,len(class_list),1):
                class_string = class_list[i]
                cpp_path = project_path + "/src/" + class_string + ".cpp" 
                h_path = project_path + "/include/" + class_string + ".h"
                
                if os.path.isfile(cpp_path) == False and os.path.isdir(project_path + "/src/") == True:
                    class_src = open(cpp_path, "w", encoding = "utf-8")
                    class_src.write('#include "'+class_string+'.h'+'"\n\n')
                    class_src.close()
                    success_class += 1
                    print("Creation source file successful: "+class_string+".cpp")
                elif os.path.isfile(cpp_path) == True:
                    print("Creation source file failure: ", cpp_path," is exists")
                else:
                    print("Creation source file failure: ", project_path, "/src/"," is not exists")

                if os.path.isfile(h_path) == False and os.path.isdir(project_path + "/include/") == True:
                    class_inc = open(h_path, "w",encoding = "utf-8")
                    class_inc.write("#ifndef _"+class_string.upper()+"_H_\n")
                    class_inc.write("#define _"+class_string.upper()+"_H_\n\n")
                    class_inc.write("class "+class_string+"\n")
                    class_inc.write("{\n")
                    class_inc.write("private:\n\n\n")
                    class_inc.write("public:\n")
                    class_inc.write("    "+class_string+"(){}\n")
                    class_inc.write("    ~"+class_string+"(){}\n")
                    class_inc.write("};\n\n")
                    class_inc.write("#endif")
                    class_inc.close()
                    success_class += 1
                    print("Creation header file successful: "+class_string+".h")
                elif os.path.isfile(h_path) == True:
                    print("Creation header file failure: ", h_path," is exists")
                else:
                    print("Creation header file failure: ", project_path, "/include/"," is not exists")


            print("Create Finished: ", success_class," files were created")
        else:
            print("Please new a projest by use 'np' or 'new project'")

    elif cmd_string == "quit" or cmd_string == "exit":
        break

