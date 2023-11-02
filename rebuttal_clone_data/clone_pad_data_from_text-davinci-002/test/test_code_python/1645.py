def solution():
    total_earnings = 400
    cost_of_ingredients = 100
    money_left = total_earnings - cost_of_ingredients
    donation_to_shelter = money_left / 2 + 10
    result = donation_to_shelter
    return result

print(solution())