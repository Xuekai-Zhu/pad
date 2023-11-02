def solution():
     needed_milk = 4
     needed_ice_cream = 12
     available_milk = 72
     available_ice_cream = 192
     total_needed = needed_milk + needed_ice_cream
     total_available = available_milk + available_ice_cream
     total_milkshakes = total_available // total_needed
     leftover_milk = available_milk - (total_needed * total_milkshakes)
     result = leftover_milk
     return result

print(solution())