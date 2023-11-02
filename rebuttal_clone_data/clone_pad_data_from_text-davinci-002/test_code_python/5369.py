def solution():
     plantation_length = 500
     plantation_width = 500
     grams_per_square_foot = 50
     grams_per_peanut_butter = 20
     grams_per_kilogram = 1000
     grams_per_kilogram_peanut_butter = 5
     dollars_per_kilogram = 10
     
     total_peanuts = plantation_length * plantation_width * grams_per_square_foot
     total_peanut_butter = total_peanuts / grams_per_peanut_butter
     total_kilograms = total_peanut_butter / grams_per_kilogram_peanut_butter
     total_dollars = total_kilograms * dollars_per_kilogram
     result = total_dollars
     return result

print(solution())