# txt2mysql
遍历文件夹，读取txt、sql文件，取每一行值，保存入库

安装库: pymysql multiprocess

运行前设置连个参数：

# 读取路径
READ_PATH = r"C:\Users\xxx\"

# 线程设置
PROCESS_NUM = 12

线程数 = 读取一个txt时一次读取的行数
