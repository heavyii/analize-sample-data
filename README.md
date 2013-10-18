
# 丢包率测试程序

## 测试程序

	烧写RadioTestC.exe

## 数据格式

data format: 前2字节是mote ID，三四字节是计数

data: 04-F2-A2-69-63-CD

04-F2 mote ID

A2-69 counter

## usage
	
采样数据保存为txt文件，使用终端python analize-data.py \[ txt 文件 ], 例如
	
	python analize-data.py sampledata.txt

输出如下

	heavey@heavey-ThinkPad-T420:~/Downloads/sample-analize$ python analize-data.py  sampledata.txt
	INFO: analize sampledata.txt
	LOST:  40598 --> 40599
	DONE: lost packet count = 1

丢包信息是LOST:  40598 --> 40599，本来应该是40598，读到的是40599，不连续
