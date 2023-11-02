def solution():
     total_square_feet = 5040
     number_of_units = 42
     square_feet_of_20_units = 8 * 4 * 20
     square_feet_of_1_unit = (total_square_feet - square_feet_of_20_units) / (number_of_units - 20)
     result = square_feet_of_1_unit
     return result

print(solution())