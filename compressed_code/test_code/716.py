def solution():
    
    stone_statues = 10
    wooden_statues = 20
    stone_cost = 20
    wooden_cost = 5
    total_stone_earnings = stone_statues * stone_cost
    total_wooden_earnings = wooden_statues * wooden_cost
    total_earnings = total_stone_earnings + total_wooden_earnings
    taxes = total_earnings * 0.1
    net_earnings = total_earnings - taxes
    result = net_earnings
    return result

print(solution())