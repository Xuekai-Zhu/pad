def solution():
     hand_crank_rate = 1 / 45
     electric_rate = 1 / 20
     difference_in_rate = electric_rate - hand_crank_rate
     time = 6
     total_difference = difference_in_rate * time
     result = total_difference
     return result

print(solution())