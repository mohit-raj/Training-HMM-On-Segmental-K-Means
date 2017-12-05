from viterbi import Viterbi

def main ():
	init_prob = [ 0, 0.5, 0.5 ]
	
	num_state = 2

	a = [ 
			[ 0, 0.5, 0.5 ],
			[ 0, 0.6, 0.4 ],
			[ 0, 0.7, 0.3 ]
	    ]
	
	b = [
			[ 0, 0, 0 ], 
			[ 0, 0.7, 0.3 ],
			[ 0, 0.2, 0.8 ]
	    ]
	
	T = 2

	offset = 1

	Viterbi.get_optimal_state_sequence (init_prob, a, b, num_state, T, offset)





if __name__ == "__main__":
	main ()