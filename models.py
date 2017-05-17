import sys

class Person:
	
	def __init__(self, repo, *args):
		self._repo = Repo()
		self._id = args[0];
		self._name = args[1];
		self._gender = args[2];
		self._birthdate = args[3];
		self._fatherID = args[4];
		self._motherID = args[5];
	
	def getID(self):
		return self._id

	def isMale(self):
		return self._gender.lower() == 'male'

	def isFemale(self):
		return self._gender.lower() == 'female'

	def getName(self):
		return self._name

	def getBirthDate(self):
		return self._birthdate

	def getFather(self):
		return self._repo.arrayofPerson[self._fatherID]

	def getMother(self):
		return self._repo.arrayofPerson[self._motherID]

	def getFatherID(self):
		return self._fatherID

	def getMotherID(self):
		return self._motherID

	def isMarried(self):
		boolean = False
		for key,value in self._repo.arrayofMarriage.items():
			if (value.getHusband() == self or value.getWife() == self) and (not value.isEnded()):
				boolean =  True
			else:
				boolean = False
		return boolean

	def isDivorced(self):
		boolean = False
		for key,value in self._repo.arrayofMarriage.items():
			if (value.getHusband() == self or value.getWife() == self) and value.isEnded():
				boolean = True
			else:
				boolean = False
		return boolean

	def isParent(self,child):
		if self.isMale():
			for key,elem in self._repo.arrayofMarriage.items():
				if child.getFather() == self:
					return True
		elif self.isFemale():
			for key,elem in self._repo.arrayofMarriage.items():
				if child.getMother() == self:
					return True		
		return False

	def isStepParent(self,child):
		if self.isMale():
			for key,elem in self._repo.arrayofMarriage.items():
				if child.getFather() != elem.getHusband() and child.getMother() == elem.getWife():
					return True
		elif self.isFemale():
			for key,elem in self._repo.arrayofMarriage.items():
				if child.getMother() != elem.getWife() and child.getFather() == elem.getHusband():
					return True
		return False

	def getSpouse(self):
		array = []
		if self.isMale():
			for key,elem in self._repo.arrayofMarriage.items():
				if elem.getHusband() == self and (not elem.isEnded()):
					array.append(elem.getWife())
		elif self.isFemale():
			for key,elem in self._repo.arrayofMarriage.items():
				if elem.getWife() == self and (not elem.isEnded()):
					array.append(elem.getHusband())
		return array

	def getFormerSpouse(self):
		array = []
		if self.isMale():
			for key,elem in self._repo.arrayofMarriage.items():
				if elem.getHusband() == self.getID() and (elem.isEnded()):
					array.append(elem.getWife())
		elif self.isFemale():
			for key,elem in self._repo.arrayofMarriage.items():
				if elem.getWife() == self.getID() and (elem.isEnded()):
					array.append(elem.getHusband())
		return array

	def getParents(self):
		array = [self.getFather(),self.getMother()]	
		return array

	def getChildren(self):
		array = []
		if self.isMale():
			for key,elem in self._repo.arrayofPerson.items():
				if elem.getFatherID() == self.getID():
					array.append(elem)
		elif self.isFemale():
			for key,elem in self._repo.arrayofPerson.items():
				if elem.getMotherID() == self.getID():
					array.append(elem)
		return array

	def getSiblings(self):
		parentarray = self.getParents()
		father = parentarray[0].getID()
		mother = parentarray[1].getID()
		array = []
		for key,elem in self._repo.arrayofPerson.items():
			if elem.getID()!=self.getID() and (elem.getFatherID() == father or elem.getMotherID() == mother):
				array.append(elem)
		return array

	def getSisters(self):
		siblingsarray = self.getSiblings()
		array = []
		for sibling in siblingsarray:
			if sibling.isFemale():
				array.append(sibling)
		return array

	def getBrothers(self):
		siblingsarray = self.getSiblings()
		array = []
		for sibling in siblingsarray:
			if sibling.isMale():
				array.append(sibling)
		return array

	def getStepChildren(self):
		partner = self.getSpouse()
		partnerid = []
		array = []
		for partners in partner:
			partnerid.append(partners.getID())
		
		if self.isMale():
			for key,elem in self._repo.arrayofPerson.items():
				if elem.getMotherID() in partnerid and elem.getFatherID() != self.getID():
					array.append(elem)
		elif self.isFemale():
			for key,elem in self._repo.arrayofPerson.items():
				if elem.getFatherID() in partnerid and elem.getMotherID() != self.getID():
					array.append(elem)
		return array

	def getStepSisters(self):
		father = self.getFather()
		mother = self.getMother()
		siblings = self.getSiblings()
		array = []
		for sibling in siblings:
			sib_mother = sibling.getMother()
			sib_father = sibling.getFather()
			if mother != sib_mother and father == sib_father and sibling.isFemale():
				array.append(sibling) 
			elif mother == sib_mother and father != sib_father and sibling.isFemale():
				array.append(sibling)
		return array

	def getStepBrothers(self):
		father = self.getFather()
		mother = self.getMother()
		siblings = self.getSiblings()
		array = []
		for sibling in siblings:
			sib_mother = sibling.getMother()
			sib_father = sibling.getFather()
			if mother != sib_mother and father == sib_father and sibling.isMale():
				array.append(sibling) 
			elif mother == sib_mother and father != sib_father and sibling.isMale():
				array.append(sibling)
		return array

	def getStepMother(self):
		array = []
		for key,elem in self._repo.arrayofMarriage.items():
			mother = elem.getWife()
			father = elem.getHusband()
			if self.getMother() != mother and self.getFather() == father:
				array.append(mother)
		return array

	def getStepFather(self):
		array = []
		for key,elem in self._repo.arrayofMarriage.items():
			mother = elem.getWife()
			father = elem.getHusband()
			if self.getMother() == mother and self.getFather() != father:
				array.append(mother)
		return array

	def getUncles(self):
		return self.getFather().getBrothers()
	
	def getAunties(self):
		return self.getFather().getSisters()

	def getGrandFathers(self):
		arr = [self.getFather().getFather(),self.getMother().getFather()]
		return arr

	def getGrandMothers(self):
		arr = [self.getFather().getMother(),self.getMother().getMother()]
		return arr

	def getGrandParents(self):
		arr = []
		arr.extend(self.getGrandFathers())
		arr.extend(self.getGrandMothers())
		return arr

	def getGrandChildren(self):
		arr = []
		for child in  self.getChildren():
			arr.extend(child.getChildren())
		return arr

	def getCousins(self):
		arr = []
		for uncle in self.getUncles():
			 arr.extend(uncle.getChildren())
		for aunt in self.getAunties():
			 arr.extend(aunt.getChildren())
		return list(set(arr))

	def getNephews(self):
		arr = []
		for sibling in self.getSiblings():
			arr.extend(sibling.getChildren())
		return list(set(arr))

	def find(self, args):pass

	def relationTo(self, person):pass

class Marriage:

	def __init__(self,repo,*args):
		self._repo = repo
		self._id = args[0];
		self._husbandID = args[1];
		self._wifeID = args[2];
		self._startdate = args[3];
		self._enddate = args[4];
		
	def getID(self):
		return self._id

	def getHusband(self):
		return self._repo.arrayofPerson[self._husbandID]

	def getWife(self):
		return self._repo.arrayofPerson[self._wifeID]

	def getHusbandID(self):
		return self._husbandID

	def getWifeID(self):
		return self._wifeID

	def getMarriageDate(self):
		return self._startdate

	def getDivorceDate(self):
		return self._enddate

	def isEnded(self):
		return self._enddate != 'null'


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class Repo(Borg):
	arrayofPerson = {}
	arrayofMarriage = {}

	def __init__(self):
		Borg.__init__(self)

	def addPerson(self,args):
		try:
			self.arrayofPerson[args.getID()] = args
		except Exception as e:
			print ("init error")
			sys.exit(1)
			
	def addMarriage(self,args):
		self.arrayofMarriage[args.getID()] = args
		
	def getPersonById(self,personid):
		return self.arrayofPerson[personid]

	def getMarriageById(self,marrid):
		return self.arrayofPerson[marrid]

	def getRelationRoot(self,person1, person2):
		i = 1
		return self.getRelationRootHelper(person1,person2,i)

	def getRelationRootHelper(self,person1, person2, distance):
		try:
			parent1 = person1.getParents()
			parent2 = person2.getParents()
			for parent in parent1:
				if parent in parent2:
					arr = [parent,distance]
					return arr
		except Exception as e:
			return
		else:
			distance = distance + 1
			getRelationRootHelper(self,parent1[0],parent2[0],distance)
			getRelationRootHelper(self,parent1[0],parent2[1],distance)
			getRelationRootHelper(self,parent1[1],parent2[0],distance)
			getRelationRootHelper(self,parent1[1],parent2[1],distance)
