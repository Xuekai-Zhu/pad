def solution():
     cost_carnation = 0.5
     cost_dozen = 4.00
     teachers = 5
     friends = 14
     total_carnations = teachers * 12 + friends
     total_cost = total_carnations * cost_carnation
 
     return total_cost

print(solution())