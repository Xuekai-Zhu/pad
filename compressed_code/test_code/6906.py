def solution():
    
    perfume_cost = 50
    christian_savings = 5
    sue_savings = 7
    christian_mowed = 4
    christian_earnings = christian_mowed * 5
    sue_walked = 6
    sue_earnings = sue_walked * 2
    total_money = christian_savings + sue_savings + christian_earnings + sue_earnings
    remaining_money = perfume_cost - total_money
    result = remaining_money
    return result

print(solution())