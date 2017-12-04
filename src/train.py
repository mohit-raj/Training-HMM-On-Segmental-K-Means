"""
train.py: Train HMM using K-means
"""
# from nltk.tokenize import word_tokenize

class Train(object):
		# constants
		CLEAR = 1
		CLOUDY = 2
		RAINY = 3
		SNOWY = 4
		MIST = 5

		WEATHER = 9
		TEMP = 10
		ATEMP = 11
		HUMIDITY = 12
		WINDSPEED = 13

	def __init__(self, num_hidden_states):
		# public
		self.dataList = []
		self.data_size = 0

		# private
		self.__num_hidden_states = num_hidden_states
		self.__init_distribution = get_initial_state_transition_probability ()
		# self.__prob_martix = [ [ 0 for x in range (num_hidden_states) ] for y in range (num_hidden_states) ]

	def load_data (self, fileName):
		# dataList = []

		file = open ( fileName, "r")	
		for line in file:
			self.data_size += 1
			self.dataList.append ( line.split (',') )
		file.close ()
		# return dataList

	def get_initial_state_transition_probability (self):
		return
