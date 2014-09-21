#!/usr/bin/env python
# -*- coding: utf-8 -*-

def somefunc(ratings):
	doc_ratings = open(ratings,'r')
	templist_rat = []
	tempDict_rat = {}
	TEMP_rat =""
	TEMP2_rat =""
	for line in doc_ratings:
		TEMP_rat =" ".join(line.split())
		TEMP2_rat =TEMP_rat.replace('"', "")
		templist_rat.append(TEMP2_rat[11:])


		#templist hefur lengd 567002
	del templist_rat[0:296]
	del templist_rat[567002:567149]


	#RATING
	boolVote_rat = False
	boolGrade_rat = False
	boolMovie_rat = False
	tempString_rat = ""
	tempVotes_rat =""
	tempGrade_rat =""
	tempMovie_rat =""
	letterIndex_rat = 0

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
				print tempMovie_rat + "ekkertbil?"
				boolVote_rat = False
				boolGrade_rat = False
				boolMovie_rat = False
				tempString_rat = ""
				tempVotes_rat =""
				tempGrade_rat =""
				tempMovie_rat =""
				letterIndex_rat = 0
				break
			tempString_rat = tempString_rat + letter
		
	#Templist er nú allar myndir sem ég til með lengd 1856586
	k = open('ratings.txt','w')
	k.write(str(tempDict))
	k.close()





#Todo parse through all the movies and find out the movies who have the imdbRating of 7 or higher

somefunc("ratings.list")


	
	