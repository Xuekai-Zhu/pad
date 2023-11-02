def solution():
    stone_statues = 10
    wooden_statues = 20
    statue_price_stone = 20
    statue_price_wooden = 5
    monthly_earnings = (stone_statues * statue_price_stone) + (wooden_statues * statue_price_wooden)
    taxes = monthly_earnings * 0.1
    total_monthly_earnings = monthly_earnings - taxes
    result = total_monthly_earnings
    return result

print(solution())