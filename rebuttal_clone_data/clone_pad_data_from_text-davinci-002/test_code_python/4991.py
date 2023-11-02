def solution():
     boys = 200 * (60/100)
     girls = 200 - boys
     boys_percentage = 67.5
     girls_percentage = 100 - boys_percentage
     required_percentage = ((girls/boys) * 100) + girls_percentage
     result = required_percentage 
     
     return result

print(solution())