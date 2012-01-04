#CreateObjCFromProtocol

## What?
这是一个帮助iOS Developer根据PM定制的协议，自动产生MVC设计模式中model的h和m文件的python脚本。将Developer从无聊没有技术含量的工作解放出来。

## How?
`python CreateObjCFromProtocol.py ./TestNumber.txt` 

## other
协议格式：
`变量名#变量类型#变量描述\r`

脚本中：
	//协议中的类型
	otypeList = ['string','boolean','int64','int']
	//要替换的类型
	ntypeList = ['NSString','BOOL','int64_t','int32_t']

注意：
如果发现未定义的变量，系统自动略过。

##About
	email:luyiyuan129@gmail.com


