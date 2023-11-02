def solution():
    house_budget = 240
    food_percentage = 60
    food_budget = house_budget * (food_percentage / 100)
    phone_percentage = 10
    phone_budget = food_budget * (phone_percentage / 100)
    total_budget = food_budget + phone_budget + house_budget
    result = total_budget
    return result

print(solution())