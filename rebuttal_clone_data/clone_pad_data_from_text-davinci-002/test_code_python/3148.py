def solution():
     cost_one = 100
     cost_two = 244
     five_times = 5
     shirt_cost = cost_one - ((cost_two - cost_one) / five_times)
     coat_cost = cost_two - shirt_cost
     result = coat_cost
     
     return result

print(solution())