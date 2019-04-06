#!/usr/bin/python2
# coding=UTF-8
#@author neo_will
#version 2019-04-02 10:39
 
import os
import os.path
import shutil
import time, datetime
 
#fpath_2018 = [1207, 1121, 1120, 1119, 1112, 1101, 1025, 1009, 0704, 0608, 0531, 0530, 0517, 0502, 0418, 0330, 0201, 0131]
#sourceDir=r"F:\LEVEL2_shanghai\2018\fpath_2018[0:]"
#des_dir=r"G:\MarketDataSupplement\shanghai\2018\fpath_2018[0:]"
#原始目录和拷贝到的目录地址
sourceDir = r"D:\tools\wj"
targetDir = r"D:\Users\wj"
copyFileCounts = 0
 
#定义拷贝文件的函数
def copyFiles(sourceDir, targetDir):
	global copyFileCounts
	print (sourceDir )
	print ("%s 当前处理文件夹%s已处理%s 个文件" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), sourceDir,copyFileCounts) )
	for f in os.listdir(sourceDir):
		sourceF = os.path.join(sourceDir, f)
		targetF = os.path.join(targetDir, f)
		if os.path.isfile(sourceF):
			#创建目录
			if not os.path.exists(targetDir):
				os.makedirs(targetDir)
			copyFileCounts += 1
 
			#文件不存在的话，或者存在但是大小存在差异不同，执行完全覆盖操作
			if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
				#二进制文件
				open(targetF, "wb").write(open(sourceF, "rb").read())
				print u"%s %s copy over" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF)
			else:
					print("%s %s is exists,please don't copy more" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF))
 
		if os.path.isdir(sourceF):
			copyFiles(sourceF, targetF)
 
if __name__ == "__main__":
	time_start = time.time()
	try:
		import psyco
		psyco.profile()
	except ImportError:
		pass
	#copyFiles(sourceDir,targetDir)
	copyFiles(r"D:\tools\wj",r"D:\Users\wj")
	time_end = time.time()
	print('totally cost', time_end - time_start)