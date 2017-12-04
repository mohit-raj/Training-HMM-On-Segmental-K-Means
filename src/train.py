"""
train.py: Train HMM using K-means
"""
# from nltk.tokenize import word_tokenize

class Train(object):

	# constants
	TEMP = 10
	ATEMP = 11
	HUMIDITY = 12
	WINDSPEED = 13
	STATES = 0

	def __init__(self, num_hidden_states):
		# public
		self.dataList = []
		self.observation = []
		self.segment = []
		self.data_size = 0
		
		# private
		self.__num_hidden_states = num_hidden_states

	def load_data (self, fileName):
		# dataList = []

		file = open ( fileName, "r")	
		for line in file:
			self.data_size += 1
			self.dataList.append ( line.split (',') )
		file.close ()


	# This will give all observation vectors.
	def get_observation (self):
		self.observation = [[] for i in range(0, self.data_size)]
		self.data_size = 0
		for i in self.dataList:
			self.observation[self.data_size].append(i[self.TEMP])
			self.observation[self.data_size].append(i[self.ATEMP])
			self.observation[self.data_size].append(i[self.HUMIDITY])
			self.observation[self.data_size].append(i[self.WINDSPEED])			
			self.data_size += 1
		return self.observation


	# This is the initial training sequence/segment
	def get_segments (self):
		#This will group 10 observation vectors in one segment. So there will be 73 such segments.
		self.segment = [[] for i in range(0, self.data_size)]
		k = -1
		for i in range(0, self.data_size):
			if(i % 10 == 0):
				k += 1
				self.segment[k].append(self.observation[i])
			else:
				self.segment[k].append(self.observation[i])
		return self.segment

		



	