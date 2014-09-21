def func():
	prufa = {}
	prufa[123] = {}
	prufa[123]["kalli2"] =[]
	prufa[123]["kalli2"].append("yloo")

	prufa[1234] = {}
	prufa[1234]["kalli2"] =[]
	prufa[1234]["kalli2"].append("yloo")

	prufa[1235] = {}
	prufa[1235]["kalli2"] =[]
	prufa[1235]["kalli2"].append("yloo")

	for keys in prufa:
		if keys == 123:
			print prufa[keys]
			print "virkar"


func()