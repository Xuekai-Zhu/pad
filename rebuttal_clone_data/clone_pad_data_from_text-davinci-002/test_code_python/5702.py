def solution():
     fuel_capacity = 150
     initial_fuel = 38
     fuel_used = fuel_capacity - initial_fuel
     price_per_liter = 3
     cost_of_fuel = fuel_used * price_per_liter
     money_given = 350
     change = money_given - cost_of_fuel
     result = change
     return result

print(solution())