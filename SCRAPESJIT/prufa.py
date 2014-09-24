#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def somefunc(genre,ratings):
	#open the docs
	doc_genre = open(genre,'r')
	doc_ratings = open(ratings,'r')

	#INIT VARS FOR READINGS
	#RATING
	templist_rat = []
	TEMP_rat =""
	TEMP2_rat =""

	#GENRE
	templist = []
	tempDict = {}
	TEMP =""
	#THE GENRES THAT ARE AVALABLE
	genres = ['Short','Drama','Comedy','Documentary','Adult','Action','Romance','Thriller','Animation','Family','Crime','Horror','Music','Adventure','Fantasy','Sci-Fi','Mystery','Sport','Musical','Western','War','Reality-TV','News','Talk-Show','Game-Show','Film-Noir','Lifestyle','Experimental','Erotica','Commercial']
	
	#GET ALL THE GENRES-------------------------------
	for line in doc_genre:
		TEMP =" ".join(line.split())
		templist.append(TEMP.replace('"', ""))
		
	del templist[0:380]
	#Templist er nú allar myndir sem ég til með lengd 1856586
	#-------------------------------------------------

	#GET ALL THE RATINGS------------------------------
	for line in doc_ratings:
		TEMP_rat =" ".join(line.split())
		TEMP2_rat =TEMP_rat.replace('"', "")
		templist_rat.append(TEMP2_rat[11:])

	
	del templist_rat[0:296]
	del templist_rat[567002:567149]
	#templist_rat hefur lengd 567002
	#------------------------------------------------

	#COLLECT THE INFO FROM THE DOCS
	#########################################################################

	#TEMPVARS

	#GENRE
	tempString = ""
	tempMovie = ""
	tempGenre = ""
	It_true = False

	#tempbreytur fyrir að setja í dataform
	tempStored = 0
	print "byrja að flokka myndir í genre"
	for movie in templist:
		for letter in movie:

			if letter == " ":
				tempString = ""

			tempString = tempString + letter

			for genre in genres:
				if genre == "".join(tempString.split()):

					It_true = True
					tempGenre = genre
					tempString =""
				
			if It_true:
				tempMovie = movie[0:len(movie)-(len(tempGenre)+1)]

				It_true = False
				break;

		#Ef þetta er fyrsti gæjinn hentu honum beint inn og uppfærðu tempbreytu í gæjan		
		if tempStored == 0:
			#set in database tempMovie is the main and append tempGenre to it
			
			tempDict[tempMovie] = {}
			tempDict[tempMovie]["genre"] = []
			tempDict[tempMovie]["genre"].append(tempGenre)

			tempStored = tempMovie

			tempGenre=""
			tempMovie=""

		#þetta er sama mynd og síðast
		elif tempStored == tempMovie:
			
			#append the current genre to the previus movie that is alredy in the database append genre
			tempDict[tempStored]["genre"].append(tempGenre)

			tempGenre=""
			tempMovie=""


		#þetta er ný mynd
		else:
			tempDict[tempMovie] = {}
			tempDict[tempMovie]["genre"] = []
			tempDict[tempMovie]["genre"].append(tempGenre)

			tempStored = tempMovie

			tempGenre=""
			tempMovie=""

##########################################################################################
	#COLLECT THE RATINGS
	#VARS
	
	#RATING
	boolVote_rat = False
	boolGrade_rat = False
	tempString_rat = ""
	tempVotes_rat =""
	tempGrade_rat =""
	tempMovie_rat =""
	letterIndex_rat = 0
	MOVIE_HAS_RATING = False
	print "byrja að flokka myndir í ratings"
	for movie in templist_rat:
		for letter in movie:
			if letter == " " and boolVote_rat == False:
				tempVotes_rat = tempString_rat
				tempString_rat = ""
				boolVote_rat = True
				continue
			elif letter == " " and boolGrade_rat == False:
				tempGrade_rat = tempString_rat
				tempString_rat = ""
				boolGrade_rat = True
				continue
			elif letter != " " and boolGrade_rat == True and boolVote_rat == True:
				letterIndex_rat = movie.index(letter)
				#maby -1
				tempMovie_rat = movie[letterIndex_rat:len(movie)]
				break
			tempString_rat = tempString_rat + letter

		#CHECKA HVORT AÐ MYNDINN SÉ TIL Í TEMPLIST
		

		if tempMovie_rat in tempDict:
			#add the rating and votes to the movie
			tempDict[tempMovie_rat]["rating"] =[]
			tempDict[tempMovie_rat]["votes"] =[]
			tempDict[tempMovie_rat]["rating"].append(tempGrade_rat)
			tempDict[tempMovie_rat]["votes"].append(tempVotes_rat)
			#set the vars to start value
			print tempDict[tempMovie_rat]
			boolVote_rat = False
			boolGrade_rat = False
			tempString_rat = ""
			tempVotes_rat =""
			tempGrade_rat =""
			tempMovie_rat =""
			letterIndex_rat = 0	
		else:

			boolVote_rat = False
			boolGrade_rat = False
			tempString_rat = ""
			tempVotes_rat =""
			tempGrade_rat =""
			tempMovie_rat =""
			letterIndex_rat = 0



	#if grade<6,5 or votes<500
	print " lengd: " + str(len(tempDict.items()))

	#vars
	has_rating = False
	has_votes = False

	print "Starting to sort the movies bro"

	#FORMAT OF DICT

	"""
	tempDict = {"movie":{rating: ["5.3"] , votes : ["6333"] , genre: ["Action","hero"]},"nextmovie" ...... }
	"""
	#Loop through all the keys (movies)
	for keys, values in tempDict.items():


		#loop throgh all the types in the keys
		#Not all movies have rating and votes so check if they have it
		has_rating = False
		has_votes = False
		for types in values:
			if types == 'rating':
				has_rating = True
			if types == 'votes':
				has_votes = True

		#If they have both rating and votes, check if they fullfill the conditions
		if has_rating == False or has_votes == False:
			tempDict.pop(keys, None)

		elif has_rating == True and has_votes == True:
			if float(values['rating'][0])< 5.0 or int(values['votes'][0])<3000:
				#del from the tempdict
				tempDict.pop(keys, None)
				

	#solve the isue with that there is a utf-8 unicode error if i dont add str() to the dict..
	#TODO
	with open('movies.json', 'wb') as fp:
		json.dump(str(tempDict), fp)




somefunc("genres.list","ratings.list")

		 	
