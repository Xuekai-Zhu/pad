def solution():
    
    stone_statues = 10
    wooden_statues = 20
    stone_price = 20
    wooden_price = 5
    total_income = (stone_statues * stone_price) + (wooden_statues * wooden_price)
    taxes = total_income * 0.1
    earnings = total_income - taxes
    result = earnings
    return result

print(solution())