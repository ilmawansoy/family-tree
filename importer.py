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


if __name__ == "__main__":
	
	repo = Repo()
	importPersonCSV('man.csv',repo)
	importMarriageCSV('marriage.csv',repo)

	person = repo.getPersonById('2')
	person2 = repo.getPersonById('8')

	#xy = repo.getRelationRoot(person,person2)
	print(person.isStepParent(person2))
	arr = person.getStepChildren()
	for x in arr:
		print (x.getName())
	#person3,dist=xy[0].getName(),xy[1]
	#print(person3)
	#print(dist)
