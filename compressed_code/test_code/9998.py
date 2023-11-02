def solution():
    
    feet_per_side = 500
    square_feet = feet_per_side ** 2
    grams_per_square_foot = 50
    total_grams = square_feet * grams_per_square_foot
    grams_per_peanut_butter = 20
    peanut_butter_ratio = 5 / 20
    peanut_butter_production = total_grams * peanut_butter_ratio
    kg_of_peanut_butter = peanut_butter_production / 1000
    price_per_kg = 10
    revenue = kg_of_peanut_butter * price_per_kg
    result = revenue
    return result

print(solution())