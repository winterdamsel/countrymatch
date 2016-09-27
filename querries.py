#!/usr/bin/python

import sys, getopt

myc = sys.argv[1]

print myc

countries = { "BR": { "Name": "Brazil", "Friends": ["MX"], "Categories": [19]}, "FI": {	"Name": "Finland",	"Friends": ["GR", "IN","MX", "TK"], "Categories": [4,5,8,10,11,14]}, "GR": { "Name": "Greece","Friends": ["IN", "KZ", "MX", "TK"],"Categories": [4, 5, 8, 10, 11, 14]}, "IN": {	"Name": "India","Friends": ["FI", "GR", "MX", "TK"],"Categories": [1, 6, 7, 9, 10, 12, 13, 14]
},"KZ": {"Name": "Kazakhstan","Friends": ["FI", "GR", "IN", "MX", "TK"],"Categories": [4, 10, 14, 20, 21, 22]},"MX": {"Name": "Mexico","Friends": ["BR", "FI", "GR", "IN", "KZ", "TK"],"Categories": [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 17, 18, 20]
},"TK": {"Name": "Turkey","Friends": ["FI", "GR", "KZ", "MX"],"Categories": [2, 3, 5, 8, 10, 11, 12, 14, 15, 20, 21]}}

categories = {1:"Colorful Festivals", 2: "String Cheese",3:"Beverage made of starch",4:"Sweet fried dough",5:"Greet with a kiss",6:"Crunchy things with sauce",7:"Sauce out of spice",8:"Mutant liqueur",9:"Flat flour-based food",10:"Big parties",11:"Drinking allowed",12:"Cardammon usage",13:"Casseroles during parties",14:"Fried dough balls and syrup",15:"Stuffed floured-based",16:"Bloody ingredients",17:"Peanut candies",18:"Easter dessert",19:"Renowned pastries",20:"Spicy sausage",21:"Salty pastries",
22:"Livery ingredients",23:"Spicy food"}

items = {1:{"Country":"IN", "Category": 1, "item": "Holi", "photo": "URL", "description": "A festival where people throw colorful dust"},2:{"Country":"MX", "Category": 1, "item": "Day of the Dead", "photo": "URL", "description": "Celebrating death"},3:{"Country":"TK", "Category": 2, "item": "Orgu peyniri", "photo": "URL", "description": "String cheese"}, 4:{"Country":"MX", "Category": 2, "item": "Queso Oaxaca", "photo": "URL", "description": "String cheese"},5:{"Country":"TK", "Category": 3, "item": "Salep", "photo": "URL", "description": "Orchid starch"},6:{"Country":"MX", "Category": 3, "item": "Atole", "photo": "URL", "description": "Corn starch"}}

#print countries["TK"]["Categories"]
things = countries[myc]["Categories"]
friends = countries[myc]["Friends"]
#print things

print "***** " +countries[myc]["Name"].upper()+" *****\n" ;
print "Similarities with : "
for idname in friends:
	print " - "+countries[idname]["Name"] 

"""
for key in categories:
	if key in things:
		print "--------------------------------------"
		print categories[key]
		print "--------------------------------------"
		for elem in items:
			if items[elem]["Category"] == key:
				print items[elem]["item"]
				print "     "+items[elem]["description"]
				print "     From: "+items[elem]["Country"]
				
"""
				################################################################

for idc in friends:
	print "______________________________________\n"
	print  countries[idc]["Name"] 
	print "______________________________________\n"
	
	for elem in items:
		if items[elem]["Country"] == idc:
			print items[elem]["item"]
			print "     "+items[elem]["description"]
			catloc = items[elem]["Category"]
			for k in items:
				if items[k]["Category"] == catloc and items[k]["Country"] == myc:
					print "\n.............and in "+countries[myc]["Name"]+"............\n"
					print items[k]["item"]
					print "     "+items[k]["description"]
					print "--------------------------------------"
			
			