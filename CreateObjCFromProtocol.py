#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

otypeList = ['string','boolean','int64','int']
ntypeList = ['NSString','BOOL','int64_t','int32_t']


def stringfordefine(atype,aname,adesc):
	if atype in otypeList:
		idx = otypeList.index(atype)
		if atype == otypeList[0]:
			return '	'+ntypeList[idx]+'	*_'+aname+';	//'+adesc+'\r'
		else:
			return '	'+ntypeList[idx]+'	_'+aname+';		//'+adesc+'\r'
	else:
		print 'we didn\'t find the type['+atype+']'
		return ''

	
def stringforproperty(atype,aname):
	if atype in otypeList:
		idx = otypeList.index(atype)
		if atype == otypeList[0]:
			return '@property (nonatomic,copy) '+ntypeList[idx]+' *'+aname+';\r'
		else:
			return '@property '+ntypeList[idx]+' '+aname+';\r'
	else:
		print 'we didn\'t find the type['+atype+']'	
		return ''

	
def stringforsyn(atype,aname):
	if atype in otypeList:
		return '@synthesize '+aname+'=_'+aname+';\r'
	else:
		return ''

def stringfordealloc(atype,aname):
	if atype in otypeList and atype == otypeList[0]:
		return '	self.'+aname+' = nil;\r'
	else:
		return ''

print 'source file is ['+sys.argv[1]+']'
f=open(sys.argv[1],'r')
file=f.readlines()
outh=open('./h.txt','w')
outm=open('./m.txt','w')


count={}
hlist=[]
mlist=[]
alldata = []
	
for line in file:
		dataStruct = {};
		dataone = line.split('#')
		tname = dataone[0].strip()
		ttype = dataone[1].strip()
		tdesc = dataone[2][:-1].strip()
		#print("[%s] [%s] [%s]" %(tname,ttype,tdesc))
		dataStruct['type'] = ttype
		dataStruct['name'] = tname
		dataStruct['desc'] = tdesc
		alldata.append(dataStruct)
#==================for the head file===============================
#define
hlist.append('{\r')
for d in alldata:
		str = stringfordefine(d['type'],d['name'],d['desc'])
		hlist.append(str)
hlist.append('}\r')
#property
for d in alldata:	
		hlist.append(stringforproperty(d['type'],d['name']))
outh.writelines(hlist)		
outh.close()

#==================for the m file===============================
for d in alldata:	
		mlist.append(stringforsyn(d['type'],d['name']))

mlist.append('-(void)dealloc\r{\r')
for d in alldata:	
		mlist.append(stringfordealloc(d['type'],d['name']))
mlist.append('	[super dealloc];\r}\r')		
		
		
outm.writelines(mlist)
outm.close()
		
f.close()

os.system('mate '+'./h.txt')
os.system('mate '+'./m.txt')


