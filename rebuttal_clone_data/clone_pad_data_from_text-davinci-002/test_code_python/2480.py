def solution():
     number_of_singers = 30
     number_of_robes = 12
     robes_needed = number_of_singers - number_of_robes
     cost_per_robe = 2
     total_cost = robes_needed * cost_per_robe
     result = total_cost
     return result

print(solution())