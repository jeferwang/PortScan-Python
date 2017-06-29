# -*- coding:utf-8 -*-
import socket
from threading import Thread

import time

result = []


def scaner(host, port):
	"""
	端口扫描函数
	如果连接成功,把端口放入result中
	否则关闭连接
	:param host:
	:param port:
	:return:
	"""
	sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sockfd.settimeout(0.1)
	print(f'正在检测{host}:{port}...')
	tryConn = sockfd.connect_ex((host, port))
	if not tryConn:  # 返回0表示连接成功
		result.append(port)
	else:
		sockfd.close()


if __name__ == '__main__':
	host = input('请输入IP地址：')
	while True:  # 尝试对端口范围进行验证
		startPort = int(input('请输入起始扫描端口：'))
		endPort = int(input('请输入终止扫描端口：'))
		if startPort >= 65536 or endPort >= 65536:
			print('端口号不能大于65535')
		else:
			break
	startTime = time.time()
	threads = []  # 线程列表
	for p in range(startPort, endPort + 1):
		t = Thread(target=scaner, args=(host, p))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	print('端口扫描完毕，端口开放结果如下')
	result.sort()  # 排序
	for p in result:  # 打印结果
		print(f'{host}:{p}')
	endTime = time.time()  # 计时
	print(f'本次端口扫描用时{endTime-startTime}秒')
