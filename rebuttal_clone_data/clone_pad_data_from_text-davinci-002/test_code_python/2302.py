def solution():
     original_price = 1950
     decrease_per_year = 35
     years = 9
     final_price = original_price - (decrease_per_year * years)
     result = final_price
     return result

print(solution())