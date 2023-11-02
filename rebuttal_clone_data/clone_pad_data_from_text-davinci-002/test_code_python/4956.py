def solution():
     long_side1 = 8
     long_side2 = 6
     short_side1 = 5
     short_side2 = 6
     top_and_bottom = 40
     total_square_inches = (2 * long_side1 * long_side2) + (2 * short_side1 * short_side2) + (2 * top_and_bottom)
     result = total_square_inches
     return result

print(solution())