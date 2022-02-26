#coding:utf-8

'''
批量执行
'''

import os
import time
import config as cfg
import uploadpic as ulp

def IsSubString(SubStrList,Str): 

    '''
    #判断字符串Str是否包含序列SubStrList中的每一个子字符串 
    #>>>SubStrList=['F','EMS','txt'] 
    #>>>Str='F06925EMS91.txt' 
    #>>>IsSubString(SubStrList,Str)#return True (or False)
    '''

    flag=True
    for substr in SubStrList: 
        if not(substr in Str): 
            flag=False
    return flag 

def GetFileList(FindPath,FlagStr=[]): 

    '''
    #获取目录中指定的文件名 
    #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 
    #>>>FileList=GetFileList(FindPath,FlagStr) # 
    '''
    FileList=[] 
    FileNames=os.listdir(FindPath) 

    if (len(FileNames)>0): 
        for fn in FileNames: 
            if (len(FlagStr)>0): 
                # 返回指定类型的文件名
                if (IsSubString(FlagStr,fn)): 
                    # fullfilename=os.path.join(FindPath,fn) 
                    FileList.append(fn) 
                else: 
                    # 默认直接返回所有文件名
                    # fullfilename=os.path.join(FindPath,fn) 
                    FileList.append(fn) 
    # 对文件名排序
    if (len(FileList)>0): 
        FileList.sort() 
    return FileList

if __name__ == '__main__':

    file_path = cfg.article_folder_path
    flag_str = ['.md']
    file_list = GetFileList(file_path, flag_str)

    for f in file_list:
        article_path = ulp.get_path(cfg.article_folder_path, f)
        new_article_path = ulp.get_path(cfg.new_article_folder_path, f)
        ulp.change_pic_path(article_path, new_article_path, 'smms')
        time.sleep(3)


