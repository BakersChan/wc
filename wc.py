#-*-coding:utf-8-*-
import os
import re
import sys
import getopt

#获取文件字符数
def cal_strs(file):
    try:
        text = open(file,'r+',encoding='UTF-8')
        count = 0
        for line in text.readlines():
            count = count + len(line)
    except:
        print("cal_strsERROR")
    finally:
        text.close()
        print("文件"+file+"的字符数为："+str(count),"\n")


#获取文件单词数
def cal_words(file):
    try:
        text = open(file,'r+',encoding='UTF-8')
        count = 0
        for line in text.readlines():
            for mark in [',','.',":",'=',"'",'"',"(",")","+","|","[","]","{","}","\\","<",">","?","/","%","^","&","*","@","!","\t","\n","#","-","_"]:
                line = line.replace(mark," ")
            #用filter过滤
            #word = line.split(" ")
            #word = list(filter(lambda x: x!="",word))
            #用正则过滤
            word = re.split(r'\s+',line)
            count = count + len(word)
            #print(word,"count"+str(count))
    except:
        print("cal_wordsERROR")
    finally:
        text.close()
        print("文件"+file+"的单词数为："+str(count),"\n")

#获取文件的行数
def cal_lines(file):
    try:
        text = open(file,'r+',encoding='UTF-8')
        count = 0
        for line in text.readlines():
            count = count+1
    except:
        print("cal_linesERROR")
    finally:
        text.close()
        print("文件"+file+"的行数为："+str(count),"\n")

#获取代码行/空行/注释行
def cal_special(file):
    try:
        text = open(file,'r+',encoding='UTF-8')
        blank_line,code_line,note_line = 0,0,0
        for line in text.readlines():
            line = line.strip('\n')
            if(re.match(r'\s+|\W+',line) or line==""):
                blank_line = blank_line + 1
                #print("空白行")
            #使用正则表达式判断代码行和注释行
            elif(re.match(r'^\s*\w+',line)):
                code_line = code_line + 1
                #print("代码行")
            elif(re.match(r'^\s*\W*([//]|[#])',line)):
                note_line = note_line + 1
                #print("注释行")
            else:
                print(line)
                print("此句暂未收录")
    except:
        print("cal_specialError")
    finally:
        text.close()
        print("文件:"+file+"\n","空白行数为："+str(blank_line)+"\n"\
            +"代码行数为："+str(code_line)+"\n"\
            +"注释行数为："+str(note_line),"\n")


#获取目录下的所有文件路径
def get_file(root_path):
    try:
        _files = []
        files = os.listdir(root_path)
        for i in range(0,len(files)):
            path = os.path.join(root_path,files[i])
            if os.path.isdir(path):
                #print("目录：",path)
                _files.append(get_file(path))
            if os.path.isfile(path):
                #print("文件：",path)
                _files.append(path)
        #print(_files)
    except:
        print("get_fileERROR")
    finally:
        return _files

#返回路径数组
def get_files(options,path):
    try:
        files = []
        #print("get_files获取的参数options：",options,"参数path：",path)
        if('-s' in options):
            files = get_file(path)
        else:
            files.append(path)
    except:
        print("get_fileERROR")
    finally:
        return files

#选择操作类型
def choose_operate(option,file):
    try:
        #print("choose_operate获取的参数option：", option, "参数file：", file)
        funcations = {'-c':cal_strs,
                '-w':cal_words,
                '-l':cal_lines,
                 '-a':cal_special}
        method = funcations.get(option,None)
    except:
        print("choose_operateERROR")
    finally:
        if method:
            method(file)

def main():
    # 获取文件
    path = sys.argv[-1]
    # 获取指令代号
    options = sys.argv[1:-1]
    # 传入指令代号及文件名，执行操作
    files = get_files(options, path)
    # print("操作文件列表：",files)
    if ("-s" in options):
        options.remove("-s")
    for file in files:
        for option in options:
            # print(option+"+"+file)
            choose_operate(option, file)

if __name__=='__main__':
    main()