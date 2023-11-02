def solution():
     number_of_pots = 3
     cost_of_pots = 20
     number_of_pans = 4
     total_cost = 100
     cost_of_pans = total_cost - (number_of_pots * cost_of_pots)
     cost_of_two_pans = cost_of_pans / number_of_pans
     result = cost_of_two_pans
     return result

print(solution())