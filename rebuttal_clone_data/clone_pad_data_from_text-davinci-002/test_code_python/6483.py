def solution():
     turnips = 2
     potatoes = 5
     desired_potatoes = 20
     desired_turnips = ((desired_potatoes / potatoes) * turnips) 
     result = desired_turnips
     return result

print(solution())