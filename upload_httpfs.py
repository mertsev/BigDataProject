# todo: подключить к hdfs и прокинуть туда файлики

#from pywebhdfs.webhdfs import PyWebHdfsClient
#from pprint import pprint

#hdfs = PyWebHdfsClient(host='hadoop01',port='50070', user_name='hadoop')

#my_data = "01010101010101010101010101010101000111 Example DataSet"
#my_file = '/examples/myfile.txt'
#hdfs.create_file(my_file, my_data.encode('utf-8'))
from hdfs import InsecureClient

client = InsecureClient('http://ec2-3-13-187-19.us-east-2.compute.amazonaws.com:14000', user='ubuntu')

client.upload('/usr/ubuntu/hadoop1','C://git//BigDataProject//testdata', n_threads=3)
