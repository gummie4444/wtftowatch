import json

def test():


	tempDict = {}
	tempDict["biomynd"] ={}
	tempDict["biomynd"]["genre"] = []
	tempDict["biomynd"]["rating"] = []
	tempDict["biomynd"]["genre"].append("112312")
	tempDict["biomynd"]["genre"].append("2")
	bla2 = False
	for key,value in tempDict.items():
		for bla in value:
			if bla == 'genre':
				print "yolo"
		print value["genre"][0]
		if bla2:
			print "whu"









test()