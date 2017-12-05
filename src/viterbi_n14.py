def get_state_sequence_from_bp (bp, stop_state, T, N):
	state_seq = [ 0 for i in range (T) ]
	state_seq [T-1] = stop_state

	curr_state = stop_state
	for t in range (T, 1, -1):
		state_seq [t - 2] = bp [t][curr_state]
		curr_state = bp [t][curr_state]
	
	return state_seq

def get_optimal_state_sequence (init_prob, a, b, N, T, o_offset):
	bp = [ [ 0 for i in range (N+1) ] for t in range (T+1) ]
	prob_matrix = [ [ 0 for i in range (N+1) ] for t in range (T+1) ]

	# Initialize probabililty matrix
	for state in range (1, N+1, 1):
		# prob_matrix [1][state] = -np.log (init_prob [state]) - np.log (b [state][o_offset])
		prob_matrix [1][state] = init_prob [state] * b [o_offset][state][1]
		bp [1][state] = 0 # start

	# Maximising probability
	for t in range (2, T+1, 1):
		max_prob = 0
		val = 0

		for state in range (1, N+1, 1):	
			for prev_state in range (1, N+1, 1):

				# val = -np.log ( prob_matrix [t-1][state] ) - np.log ( a [prev_state][state] ) - np.log ( b [state][o_offset + t - 1] )
				val = prob_matrix [t-1][prev_state] * a [prev_state][state] * b [o_offset][state][t]
				if val > max_prob:
					max_prob = val
					prev_optimal_state = prev_state
			
			if prev_optimal_state == -1:
				print ("Somethings wrong: prev state -1")
			
			prob_matrix [t][state] = max_prob
			bp [t][state] = prev_optimal_state
	
	max_stop_state = -1
	max_prob = 0
	for state in range (1, N+1, 1):
		if prob_matrix [T][state] > max_prob:
			max_prob = prob_matrix [T][state]
			max_stop_state = state
	
	print (Viterbi.get_state_sequence_from_bp (bp, max_stop_state, T, N))
				
	
