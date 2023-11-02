def solution():
    """Matt has a peanut plantation that is 500 feet by 500 feet. 1 square foot of peanuts can make 50 grams of peanuts. If it takes 20 grams of peanuts to make 5 grams of peanut butter and 1 kg of peanut butter sells for $10 how much does he make from his plantation?"""
    plantation_area = 500 * 500
    peanut_production = plantation_area * 50
    peanut_butter_production = peanut_production / 20 * 5
    peanut_butter_in_kg = peanut_butter_production / 1000
    profit = peanut_butter_in_kg * 10
    result = profit
    return result

print(solution())