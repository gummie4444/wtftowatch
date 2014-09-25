from pymongo import MongoClient
import json

json_data = open('movies.json')

data = json.load(json_data,'latin-1')


connection = MongoClient("mongodb://gummi:gummi@ds039850.mongolab.com:39850/movies")

db = connection.movies.datas


for key,value in data.items():
	print "bla"
	movie ={'movieName':key.encode('utf-8'),'genre':[i.encode('utf-8') for i in value['genre']],'rating':value['rating'][0].encode('utf-8'),'votes':value['votes'][0].encode('utf-8')}
	db.insert(movie)

connection.close()