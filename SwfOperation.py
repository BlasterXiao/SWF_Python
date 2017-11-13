#coding=utf-8
'''
    功能介绍：
            1.完成对swf文件中swc和swz的分类
            2.完成对swc,swz文件的解压

    二〇一七年十一月十三日 09:59:36
'''
import os
import shutil
import swfunzip

#显示功能列表
def ShowUi():
    print ("...........功能列表..................\r\n");
    print ("1.对swf文件进行分类                   \r\n");
    print ("2.对swc,swz文件进行解压                \r\n");
    print ("......................................\r\n");
    return 0;

#对目录的操作
def DirectoryOperation():
    while 1:
        try:
            print "请输入文件路径例如：C:\\123 \r\n";
            filepath = raw_input();
            break;
        except BaseException, e:
            print "%s" % (e);

    #检测是否是个正常目录
    while 1:
        try:
            if (os.path.isdir(filepath)):
                break;
            else:
                print "请重新输入文件路径例如：C:\\123 \r\n";
                filepath = input();
        except BaseException, e:
            print ("异常：%s\r\n", e);

    #检测是否有swf,swc,swz目录
    while 1:
        try:
            if (os.path.isdir(filepath + '\\swf')):
                break;
            else:
                os.mkdir(filepath + '\\swf');
        except BaseException, e:
            print ("异常：%s\r\n", e);

    while 1:
        try:
            if (os.path.isdir(filepath + '\\swc')):
                break;
            else:
                os.mkdir(filepath + '\\swc');
        except BaseException, e:
            print ("异常：%s\r\n", e);

    while 1:
        try:
            if (os.path.isdir(filepath + '\\swz')):
                break;
            else:
                os.mkdir(filepath + '\\swz');
        except BaseException, e:
            print ("异常：%s\r\n", e);

    return filepath;

#文件分类
def FileClassification():

    #目录操作
    filepath = DirectoryOperation();

    pathDir =  os.listdir(filepath);
    for allDir in pathDir:
        print allDir
        if (os.path.isdir(filepath + "\\" + allDir)):
            print "目录-----> %s " % filepath + "\\" + allDir;
            continue;
        fopen = open(filepath + "\\" + allDir, 'r+');
        a = fopen.read(3);
        if (a == "FWS"):
           fopen.close();
           #移动到里面
           shutil.move(filepath + "\\" + allDir, filepath + '\\swf');
        if (a == "CWS"):
            fopen.close();
            # 移动到里面
            shutil.move(filepath + "\\" + allDir, filepath + '\\swc');
        if (a == "ZWS"):
            fopen.close();
            # 移动到里面
            shutil.move(filepath + "\\" + allDir, filepath + '\\swz');

    return 0;

#解压swc,swz
def DecompressionSWF():

    #目录操作
    filepath = DirectoryOperation();

    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        print allDir;
        if (os.path.isdir(filepath + "\\" + allDir)):
            print "目录-----> %s " % filepath + "\\" + allDir;
            continue;
        fopen = open(filepath + "\\" + allDir, 'r+');
        a = fopen.read(3);
        if (a == "CWS" or a == "ZWS"):
           fopen.close();

        os.system('python swfunzip.py '+ filepath + "\\" + allDir + " " + filepath + '\\swf\\' + allDir);

    return 0;

#选择功能
def Function():
    while (1):
        ShowUi();
        while 1:
            try:
                Number = input();
                break;
            except BaseException, e:
                print ("异常：%s\r\n", e);

        if (Number == 1):
            FileClassification();
        elif (Number == 2):
            DecompressionSWF();
        else:
            break;

    return 0;

if __name__ == '__main__':
    Function();
