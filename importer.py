from models import Repo, Person, Marriage
import csv

def importPersonCSV(filePath,repo):
	with open(filePath, newline='') as f:
   		reader = csv.reader(f)
   		reader = list(reader)
   		for row in reader:
   			personid,name,gender,birthdate,fatherid,motherid = row[0][:-1].split(';')
   			person = Person(repo,personid,name,gender,birthdate,fatherid,motherid)
   			repo.addPerson(person)
	return repo

def importMarriageCSV(filePath,repo):
	with open(filePath, newline='') as f:
		reader = csv.reader(f)
		reader = list(reader)
		for row in reader:
			marrid,husbandid,wifeid,startdate,enddate = row[0][:-1].split(';')
			marriage = Marriage(repo,marrid,husbandid,wifeid,startdate,enddate)
			repo.addMarriage(marriage)
	return repo
