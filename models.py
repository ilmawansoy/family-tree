import sys


class Person:
	
	def __init__(self, repo, *args):
		self.repo = Repo()
		self._id = args[0];
		self._name = args[1];
		self._gender = args[2];
		self._birthdate = args[3];
		self._fatherID = args[4];
		self._motherID = args[5];
		
		self._fspouse = set()
		self._children = set()
		self._spouse = None

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

	def addChildren(self, person):
		self._children.add(person)

	def addSpouse(self, person):
		self._spouse = person

	def removeSpouse(self, person):
		self._fspouse.add(person)
		if self._spouse == person:
			self._spouse = None

	def getFather(self):
		try:
			return self.repo.arrayofPerson[self._fatherID]
		except:
			return None

	def getMother(self):
		try:
			return self.repo.arrayofPerson[self._motherID]
		except:
			return None

	def getFatherID(self):
		return self._fatherID

	def getMotherID(self):
		return self._motherID

	def isMarried(self):
		return self._spouse != None

	def isDivorced(self):
		self._fspouse.add(self._spouse)
		return self._spouse == None
	
	def isParent(self,child):
		if child in self._children:
			return True
		return False

	def isStepParent(self,child):
		childparent = child.getParents()
		if self._spouse in childparent and self not in childparent:
			return True
		return False

	def getSpouse(self):
		return self._spouse

	def getFormerSpouse(self):
		return list(self._fspouse)

	def getParents(self):
		array = [self.getFather(), self.getMother()]	
		return array

	def getChildren(self):
		return list(self._children)

	def getSiblings(self):
		array = []
		parentarray = self.getParents()
		
		fatherchild = parentarray[0].getChildren()
		array.extend(fatherchild)
		
		motherchild = parentarray[1].getChildren()
		array.extend(motherchild)

		return list(set(array))

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
		partnerchild = self._spouse.getChildren()
		childs = self.getChildren()
		array = []

		for pchild in partnerchild:
			if pchild not in childs:
				array.append(pchild)
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
		for key,elem in self.repo.arrayofMarriage.items():
			mother = elem.getWife()
			father = elem.getHusband()
			if self.getMother() != mother and self.getFather() == father:
				array.append(mother)
		return array

	def getStepFather(self):
		array = []
		for key,elem in self.repo.arrayofMarriage.items():
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
		childs = self.getChildren()
		for child in childs:
			arr.extend(child.getChildren())
		return arr

	def getCousins(self):
		arr = []
		uncles = self.getUncles()
		aunties = self.getAunties()
		for uncle in uncles:
			 arr.extend(uncle.getChildren())
		for aunt in aunties:
			 arr.extend(aunt.getChildren())
		return list(set(arr))

	def getNephews(self):
		arr = []
		siblings = self.getSiblings()
		for sibling in siblings:
			arr.extend(sibling.getChildren())
		return list(set(arr))

	def find(self, args):
		args = args.lower()
		cmd = args.split(" of ")
		person = (self)
		for command in cmd:
			temp = set()
			if(cmd == 'spouse'):
				for p in person:
					temp |= (p.getSpouse())
			elif (cmd == 'former spouse'):
				for p in person:
					temp |= (p.getFormerSpouse())
			elif (cmd == 'parents'):
				for p in person:
					temp |= (p.getParents())
			elif (cmd == 'siblings'):
				for p in person:
					temp |= (p.getSiblings())
			elif (cmd == 'children'):
				for p in person:
					temp |= (p.getChildren())
			elif (cmd == 'sisters'):
				for p in person:
					temp |= (p.getSisters())
			elif (cmd == 'brothers'):
				for p in person:
					temp |= (p.getBrothers())
			elif (cmd == 'step children'):
				for p in person:
					temp |= (p.getStepChildren())
			elif (cmd == 'step sisters'):
				for p in person:
					temp |= (p.getStepSisters())
			elif (cmd == 'step brothers'):
				for p in person:
					temp |= (p.getStepBrothers())
			elif (cmd == 'step mother'):
				for p in person:
					temp |= (p.getStepMother())
			elif (cmd == 'step father'):
				for p in person:
					temp |= (p.getStepFather())
			elif (cmd == 'uncles'):
				for p in person:
					temp |= (p.getUncles())
			elif (cmd == 'aunties'):
				for p in person:
					temp |= (p.getAunties())
			elif (cmd == 'grand fathers'):
				for p in person:
					temp |= (p.getGrandFathers())
			elif (cmd == 'grand mothers'):
				for p in person:
					temp |= (p.getGrandMothers())
			elif (cmd == 'grand children'):
				for p in person:
					temp |= (p.getGrandChildren())
			elif (cmd == 'grand parents'):
				for p in person:
					temp |= (p.getGrandParents())
			elif (cmd == 'cousins'):
				for p in person:
					temp |= (p.getCousins())
			elif (cmd == 'nephews'):
				for p in person:
					temp |= (p.getNephews())
			person = temp
		return person		


	def relationTo(self, person):
		pass


class Marriage:

	def __init__(self,repo,*args):
		self.repo = repo
		self._id = args[0];
		self._husbandID = args[1];
		self._wifeID = args[2];
		self._startdate = args[3];
		self._enddate = args[4];
		
	def getID(self):
		return self._id

	def getHusband(self):
		try:
			return self.repo.arrayofPerson[self._husbandID]
		except:
			return None

	def getWife(self):
		try:
			return self.repo.arrayofPerson[self._wifeID]
		except:
			return None

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

	def addPerson(self,person):
		try:
			self.arrayofPerson[person.getID()] = person
			father = person.getFatherID()
			mother = person.getMotherID()
		
			#dummy
			if father not in self.arrayofPerson:
				self.arrayofPerson[father] = Person(person.repo,father,'male',None,None,None,None)
			#dummy
			if mother not in self.arrayofPerson:
				self.arrayofPerson[mother] = Person(person.repo,mother,'female',None,None,None,None)
			
			person.getMother().addChildren(person)
			person.getFather().addChildren(person)
		
		except Exception as e:
			print ("init error")
			sys.exit(1)
			
	def addMarriage(self, marriage):
		try:
			self.arrayofMarriage[marriage.getID()] = marriage
			wife = marriage.getWife()
			husband = marriage.getHusband()
		
			if not marriage.isEnded():
				wife.addSpouse(husband)
				husband.addSpouse(wife)
			elif marriage.isEnded():
				wife.removeSpouse(husband)
				husband.removeSpouse(wife)

		except Exception as e:
			print ("init error")
			sys.exit(1)

	def getPersonById(self,personid):
		return self.arrayofPerson[personid]

	def getMarriageById(self,marrid):
		return self.arrayofPerson[marrid]

	def getRelationRoot(self,person1, person2):
		set1 = {person1}
		set2 = {person2}
		distance = 0
		array1 = person1.getParents()
		array2 = person2.getParents()
		while len(set1 & set2) == 0: 
			temp1 = set()
			temp2 = set()
			distance += 1
			for parent in array1:
				set1 |= {parent}
				if parent.getFather() != None:
					temp1.add(parent.getFather())
				if parent.getMother() != None:
					temp1.add(parent.getMother())
			for parent in array2:
				set2 |= {parent}
				if parent.getFather() != None:
					temp2.add(parent.getFather())
				if parent.getMother() != None:
					temp2.add(parent.getMother())
			array1 = list(temp1)
			array2 = list(temp2)
		return list(set1 & set2),distance
