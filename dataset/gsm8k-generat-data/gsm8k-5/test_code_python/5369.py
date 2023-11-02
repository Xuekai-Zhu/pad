def solution():
    plantation_area = 500 * 500  # Matt's plantation is 500 feet by 500 feet
    peanut_production = plantation_area * 50  # 1 square foot of peanuts can make 50 grams of peanuts
    peanut_butter_production = peanut_production / 20 * 5  # 20 grams of peanuts make 5 grams of peanut butter
    peanut_butter_production_in_kg = peanut_butter_production / 1000  # Convert peanut butter production to kg
    revenue = peanut_butter_production_in_kg * 10  # 1 kg of peanut butter sells for $10
    result = revenue
    return result

print(solution())