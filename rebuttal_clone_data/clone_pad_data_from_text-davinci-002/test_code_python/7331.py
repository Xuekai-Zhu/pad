def solution():
     big_bottle_size = 30
     small_bottle_size = 6
     big_bottle_cost = 2700
     small_bottle_cost = 600
     number_of_small_bottles = big_bottle_size / small_bottle_size
     cost_of_small_bottles = number_of_small_bottles * small_bottle_cost
     cost_savings = cost_of_small_bottles - big_bottle_cost
     result = cost_savings
     return result

print(solution())