def solution():
     initial_money = 500
     cost_potatoes = 2
     cost_tomato = 3
     cost_cucumber = 4
     cost_banana = 5
     kilos_potatoes = 6
     kilos_tomato = 9
     kilos_cucumbers = 5
     kilos_bananas = 3
     cost_total = (kilos_potatoes * cost_potatoes) + (kilos_tomato * cost_tomato) + (kilos_cucumbers * cost_cucumber) + (kilos_bananas * cost_banana)
     remaining_money = initial_money - cost_total
     result = remaining_money
     return result

print(solution())