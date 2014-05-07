import os, re, nltk, csv, datetime, subprocess
from pymongo import MongoClient
from pprint import pprint


class senna:
	'Class of Senna Objects'
	def __init__(self, input, collection = 'test'):
		self.input = input
		self.collection = collection
		self.c = MongoClient('localhost', 27017)
		self.db = self.c['nlp'][self.collection]
		self.post_ids = []

	def sennaShell(self, inputFile, outputFile):
		os.chdir('/Users/charleywu/Desktop/senna')
		cmd= "./senna <'%s'> '%s'" %  (inputFile, outputFile)
		subprocess.call(cmd, shell=True)	#todo: shell=True can be harmful; find server based method to run Senna

	def lemma(self, verb):
		wnl = nltk.WordNetLemmatizer()
		lem = wnl.lemmatize(verb,'v').lower()
		return lem

	def thetaSearch(self, term):
		regex = re.compile(r'A[0-9]')
		m = regex.search(term)
		if m is not None:
			return m.group(0)
		else:
			return None
	def verbSearch(self, term):
		regex = re.compile(r'S-V')
		m = regex.search(term)
		if m is not None:
			return m.group(0)
		else:
			return None		
	def verbNetRole(self, verb, position):
		regex = re.compile(r'[0-9]')
		m = regex.search(position)
		if m is not None:
			position = int(m.group(0))
		else:
			position = 0
		verbnet = self.c['nlp']['verbnet']
		vb = verbnet.find_one({'members':verb})
		if vb is not None:
			roles = vb.get('thematicRoles',[])
			#todo: find more elegant method if senna provides more thetaroles than verbnet does
			if (position >= (len(roles)-1)):
				return roles[0]
			else:
				return roles[position]
		else:
			return 'None'

	#main function, where self.input points to a .txt file
	#todo: upgrade method to process the entire input text and run sentence detection at the db insertion end
	def call(self, **kwargs):
		#specify intermediate file and output file
		intermediate = kwargs.get('intermediate', '/Users/charleywu/Desktop/senna/examples/input.txt')
		outputFile = kwargs.get('outputFile', '/Users/charleywu/Desktop/senna/examples/output.csv')
		#read input file and separate into sentences
		inputFile = self.input
		with open(inputFile, 'r') as f:
			text = f.read()
			#separate into sentences
			sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
			sents = sent_tokenizer.tokenize(text)
			#loop through each sentence and pass it through to senna
			sentencePosition = 0
			for sent in sents:
				sent = sent.replace('\n','')
				sentencePosition += 1
				#create database object for sentence
				post = {'text': sent, 'ts': datetime.datetime.utcnow(), 'sentencePosition':sentencePosition}
				post_id = self.db.insert(post)
				self.post_ids.append(post_id)
				#Pass sentence through to Senna
				with open(intermediate, 'wb') as file:
					file.write(sent)
				self.sennaShell(intermediate, outputFile)
				#read senna output and create a JSON object for each individual token
				with open(outputFile, 'rb') as output:
				    cr = csv.reader(output, delimiter='\t') 
				    tokenPosition = 0
				    for row in cr:
				    	if len(row) > 0:
					    	tokenPosition += 1
					    	token = row[0].strip()
					    	pos = row[1].strip()
					    	chk = row[2].strip()
					    	ner = row[3].strip()
					    	verb = row[4].strip() 	
					    	thetaList = []
					    	thetas = row[5:-1]
					    	for theta in thetas:	
					    		theta = theta.strip()
					    		thetaList.append(theta)
					    	_token = ' '+token.replace('\\','')	#remove any '\' from text
					    	syntax = re.sub('\*',_token,row[-1].strip())
					    	verbLemma = self.lemma(verb)
					    	#JSON output
					    	post = {
					    			'position': tokenPosition,
						    		'token': token,
						    		'pos': pos,
						    		'chk': chk,
						    		'ner': ner,
					    			'verb': verbLemma,
					    			'thetaList': thetaList,
					    			'syntax': syntax
					    	}
					    	#find parent and add member
					    	self.db.update({"_id":post_id},{"$push":{"members":post}})
					    	self.db.update({"_id":post_id},{"$push":{"tokenList":token}})
			    			if verb is not "-":
			    				self.db.update({"_id":post_id},{"$push":{"verbList":verbLemma}})
					    	self.db.update({'_id':post_id},{'$set':{'thetaCount': len(thetaList)}})
					    	self.db.find_one({'_id':post_id})
			return self.post_ids

	def callFromString(self, **kwargs):
		#create a JSON object and insert it into mongo
		post = {'text': self.input, 'ts': datetime.datetime.utcnow()}
		post_id = self.db.insert(post)
		self.post_ids = [post_id]	#Senna.post_id can be used to access the 
		#create input and ouput files in 'Users/charleywu/Desktop/senna/examples' unless specified in the kwargs
		inputFile = kwargs.get('inputFile', '/Users/charleywu/Desktop/senna/examples/input.txt')
		outputFile = kwargs.get('outputFile', '/Users/charleywu/Desktop/senna/examples/output.csv')
		with open(inputFile, 'wb') as file:
			file.write(self.input)
			file.close()
		#run Senna on the input file and write the output to the same directory as output.csv
		self.sennaShell(inputFile, outputFile)
		#read csv output and create a JSON object
		with open(outputFile, 'rb') as output:
		    cr = csv.reader(output, delimiter='\t') #target csv location
		    position = 0
		    for row in cr:
		    	if len(row) > 0:
			    	position += 1
			    	token = row[0].strip()
			    	pos = row[1].strip()
			    	chk = row[2].strip()
			    	ner = row[3].strip()
			    	verb = row[4].strip()
			    	thetaList = []
			    	thetas = row[5:-1]
			    	for theta in thetas:	
			    		theta = theta.strip()
			    		thetaList.append(theta)
			    	_token = ' '+token.replace('\\','')	#remove any '\' from text
			    	syntax = re.sub('\*',_token,row[-1].strip())
			    	verbLemma = self.lemma(verb)
			    	#JSON output
			    	post = {
			    			'position': position,
				    		'token': token,
				    		'pos': pos,
				    		'chk': chk,
				    		'ner': ner,
			    			'verb': verbLemma,
			    			'thetaList': thetaList,
			    			'syntax': syntax
			    	}
			    	#find parent and add member
			    	self.db.update({"_id":post_id},{"$push":{"members":post}})
			    	self.db.update({"_id":post_id},{"$push":{"tokenList":token}})
			    	if verb is not "-":
			    		self.db.update({"_id":post_id},{"$push":{"verbList":verbLemma}})
			    	self.db.update({'_id':post_id},{'$set':{'thetaCount': len(thetaList)}})
			    	self.db.find_one({'_id':post_id})
		output.close()
		return post_id

	def drawTree(self, post_id):
		entry = self.db.find_one({'_id':post_id})
		print type(entry)
		schemaList = []
		for member in entry['members']:
			#todo: sort by member['position']
			syntax = member.get('syntax', None)
			schemaList.append(syntax)
		schema = ''.join(schemaList)
		print schema
		tree = nltk.Tree(schema)
		tree.draw()
		print member

	def roleLabel(self):
		#loop through each sentence
		for post_id in self.post_ids:
			post = self.db.find_one({'_id':post_id})
			thetaCount = post.get('thetaCount', 0)
			#column by column
			for argument in range(thetaCount):
				themes = {}
				#find 'S-V' in thetaList[argument] to identify verb
				for member in post.get('members',{}):
					thetaList = member.get('thetaList',[])
					elem = thetaList[argument]
					if self.verbSearch(elem) is not None:
						themes['verb'] = self.lemma(member.get('token',''))
				themes['roles'] = dict()
				#loop through each token of the sentence to assign thematic role from theta role
				verb = themes['verb']
				for member in post.get('members',{}):
					thetaList = member.get('thetaList',[])
					token = member.get('token','')
					elem = thetaList[argument]
					position = self.thetaSearch(elem)
					if position is not None:
						thetaRole = self.verbNetRole(verb, position)
						entry = (token, elem)
						if thetaRole not in themes['roles']:
							themes['roles'][thetaRole] = list()
						themes['roles'][thetaRole].append(entry)
				self.db.update({'_id':post_id},{'$push':{'arguments':themes}})
		return themes