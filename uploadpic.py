#!usr/bin/env python
# -*- coding:utf-8 _*-

'''
@File    ：uploadpic.py
@Author  ：nifanle
@Date    ：2022-02-26
'''

import re
import argparse
import os
import shutil
import smms as sm
import config as cfg

def get_path(folder_path, title):
    '''
        合成文章路径
        '''
    try:
        # 文章目录在 config 中配置
        path = os.path.join(folder_path, title)
        return path
    except BaseException as err:
        print("error in get_article_path\n{}".format(err))

def change_pic_path(article_path,new_article_path, upld_method):
    '''
        article_path: 文章的本地路径
        upld_method: 上传方法，目前仅支持 sm.ms
        '''
    print("please wait a moment")
    try:
        with open(article_path, 'r', encoding='utf-8') as md:
            article_content = md.read()
            new_article_content = ''
            pic_block = re.findall(r'\!\[.*?\)', article_content)  # 获取添加图片的 Markdown 文本
            if upld_method == "smms":
                for i in range(len(pic_block)):
                    pic_origin_md_url = re.findall(r'\((.*?)\)', pic_block[i])[0]  # 获取插入图片时 md 中图片的位置
                    if (':' not in pic_origin_md_url):
                        pic_name = pic_origin_md_url.split('/')[-1]  # 获取插入图片时 md 中图片的名
                        pic_origin_url = os.path.join(cfg.image_folder_path, pic_name)  # 获取插入图片的全路径，图片路径在 config 中配置
                        # 本地图片路径正确才会执行上传
                        if (os.path.exists(pic_origin_url)):
                            pic_new_url = smms(pic_origin_url)
                            print("pic_new_url is {}".format(pic_new_url))
                            article_content = article_content.replace(pic_origin_md_url, pic_new_url)
                            new_article_content = article_content

                        else:
                            print("get_pic_path error")

            else:
                print("get_pic_path error")

        if (len(new_article_content)>0):
            copyfile(article_path, new_article_path)
            with open(new_article_path, 'w', encoding='utf-8') as md:
                md.write(new_article_content)
                print("job done")


    except BaseException as err:
        print("error in change_pic_path\n{}".format(err))

# 复制文件
def copyfile(source_path, target_path):
    # assert not os.path.isabs(source_path)
    # target_path = os.path.join(target, os.path.dirname(source))

    # create the folders if not already exists
    # os.makedirs(target_path)

    # adding exception handling
    try:
        shutil.copy(source_path, target_path)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())

# 上传至 SM.MS
def smms(pic_origin_url):
    try:
        sm.root = cfg.sm_api_url
        smms = sm.SMMS(cfg.sm_username, cfg.sm_password)
        smms.get_api_token()
        smms.upload_image(pic_origin_url)
        cloud_path = smms.url
        return (cloud_path)

    except BaseException as err:
        print("error in smms\n{}".format(err))


if __name__ == '__main__':

    # 解析命令行
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands", dest="command")

    smms_parser = subparsers.add_parser("smms", help="use smms")
    smms_parser.add_argument("art_title", help="input filename")

    local_parser = subparsers.add_parser("local", help="use local")
    local_parser.add_argument("art_title", help="input filename")

    args = parser.parse_args()

    # 获取配置文件中的文件夹路径
    article_path = get_path(cfg.article_folder_path, args.art_title)
    new_article_path = get_path(cfg.new_article_folder_path, args.art_title)

    if args.command == "smms":
        change_pic_path(article_path, new_article_path, 'smms')