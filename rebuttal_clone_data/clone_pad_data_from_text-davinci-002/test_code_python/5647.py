def solution():
     miles_to_home = 220
     mpg = 20
     gallons_in_tank = 16
     gallons_used = miles_to_home / mpg
     gallons_left = gallons_in_tank - gallons_used
     miles_after_home = gallons_left * mpg
     result = miles_after_home
     return result

print(solution())