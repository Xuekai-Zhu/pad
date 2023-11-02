def solution():
     pattern_cost = 15
     thread_cost = 6
     fabric_cost = 24
     total_cost = 141
     yards_bought = (total_cost - pattern_cost - thread_cost) / fabric_cost
     result = yards_bought
     return result

print(solution())