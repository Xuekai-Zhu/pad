def solution():
     initial_bear_cost = 4
     discount_per_bear = .5
     number_of_bears = 101
     total_cost = initial_bear_cost + (number_of_bears - 1) * discount_per_bear
     result = total_cost
     return result

print(solution())