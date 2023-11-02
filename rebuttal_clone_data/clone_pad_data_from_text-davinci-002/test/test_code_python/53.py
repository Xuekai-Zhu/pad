def solution():
     
     beef_ordered = 1000
     chicken_ordered = beef_ordered * 2
     beef_cost = beef_ordered * 8
     chicken_cost = chicken_ordered * 3
     total_cost = beef_cost + chicken_cost
     
     return total_cost

print(solution())