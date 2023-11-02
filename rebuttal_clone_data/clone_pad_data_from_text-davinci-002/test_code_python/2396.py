def solution():
     mountain_dew_cans = 6
     ice_ounces = 28
     fruit_juice_ounces = 40
     ounces_in_a_gallon = 128
     gallons_in_a_punch = ((mountain_dew_cans * 12) + ice_ounces + fruit_juice_ounces) / ounces_in_a_gallon
     ounces_in_a_serving = 10
     servings = gallons_in_a_punch * ounces_in_a_gallon / ounces_in_a_serving
     result = servings
     return result

print(solution())