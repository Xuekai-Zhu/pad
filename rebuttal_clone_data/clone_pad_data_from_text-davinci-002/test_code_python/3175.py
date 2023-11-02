def solution():
     streets_ew = 18
     streets_ns = 10
     miles_ew = 2
     miles_ns = 4
     miles_total = (streets_ew * miles_ew) + (streets_ns * miles_ns)
     cost_per_mile = 2000
     total_cost = miles_total * cost_per_mile
     result = total_cost
     return result

print(solution())