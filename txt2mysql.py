# -*- coding: utf-8 -*-

import os
import pymysql
import warnings
from multiprocess import Pool
warnings.filterwarnings("ignore")

# 读取路径
READ_PATH = r"C:\Users\MangZhong\Downloads"

# 线程设置
PROCESS_NUM = 12

# MYSQL 配置
HOST      = "119.3.55.220"
PORT      = 6789
USER      = "4287e7ae11008807e536c6283f82ea2f"
PASSWORD  = "2tU4yyHkwu"
DATABASE  = "jrj"
TABLE     = "read_from_file"

def link_mysql():
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
        return conn
    except Exception as e:
        print("\n数据库连接失败：%s\n请检查MYSQL配置！\n" % e)

def save_data(line):
    try:
        sql = "INSERT IGNORE INTO %s" % TABLE + "(mobile) VALUES(%s)" % line
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("\n保存数据失败：%s\n" % e)

def get_all_file():
    try:
        file_paths = []
        
        for parent, dirname, filenames in os.walk(READ_PATH):
            for filename in filenames:
                if filename[-4:] == ".txt":
                    file_path = os.path.join(parent, filename)
                    file_paths.append(file_path)

        return file_paths
    except Exception as e:
        print("\n文件路径读取失败：%s\n" % e)

def read_file(paths):
    for file_path in paths:
            print("\nReading file %s\n" % file_path)

            f = open(file=file_path, mode="r")

            # 单线程
            # for line in f.readlines():
              #   line = line.strip()                
              #   save_data(line)

            # 多线程
            pool = Pool(processes=PROCESS_NUM)
            pool.map(save_data, [line.strip() for line in f.readlines()])
                
            f.close()


if __name__ == "__main__":
    try:
        conn = link_mysql()
        cursor = conn.cursor()
        file_paths = get_all_file()
        read_file(file_paths)
    except Exception as e:
        print("\n程序出错：%s\n" % e)
