def solution():
    
    money = 480
    food_spending = money / 2
    money_left_after_food = money - food_spending
    glasses_spending = money_left_after_food / 3
    money_left = money_left_after_food - glasses_spending
    result = money_left
    return result

print(solution())