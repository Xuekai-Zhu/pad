def solution():
     toothpaste_grams = 105
     dad_grams = 3
     mom_grams = 2
     anne_grams_1 = 1
     anne_grams = anne_grams_1
     brother_grams_1 = 1
     brother_grams = brother_grams_1
     family_grams = dad_grams + mom_grams + anne_grams + brother_grams
     brushes_per_day = 3
     days_for_toothpaste = toothpaste_grams / (family_grams * brushes_per_day)
     result = days_for_toothpaste
     
     return result

print(solution())