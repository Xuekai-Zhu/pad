def solution():
     cups_of_coffee = 5
     fluid_oz_per_cup = 8
     total_fluid_oz = cups_of_coffee * fluid_oz_per_cup
     percent_decrease = 50
     decrease_amount = total_fluid_oz * (percent_decrease / 100)
     fluid_oz_after_shrinkage = total_fluid_oz - decrease_amount
     result = fluid_oz_after_shrinkage
     return result

print(solution())