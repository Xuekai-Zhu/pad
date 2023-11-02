def solution():
     number_of_backpacks = 5
     cost_per_backpack = 20
     monogramming_cost = 12
     percent_off = 20
     cost_of_backpacks = number_of_backpacks * cost_per_backpack
     cost_after_discount = cost_of_backpacks - (cost_of_backpacks * (percent_off/100))
     total_cost = cost_after_discount + (number_of_backpacks * monogramming_cost)
     result = total_cost
     return result

print(solution())