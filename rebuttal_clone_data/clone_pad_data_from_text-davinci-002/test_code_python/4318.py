def solution():
 	cup_of_coffee = 4
 	piece_of_cake = 7
 	bowl_of_ice_cream = 3
 	mell_cost = cup_of_coffee + piece_of_cake
 	friend1_cost = cup_of_coffee + piece_of_cake + bowl_of_ice_cream
 	friend2_cost = cup_of_coffee + piece_of_cake + bowl_of_ice_cream
 	total_cost = mell_cost + friend1_cost + friend2_cost
 	result = total_cost
 	return result

print(solution())