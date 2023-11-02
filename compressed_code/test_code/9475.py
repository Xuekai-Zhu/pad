def solution():
    
    monday_bags = 5
    tuesday_bags = 3
    total_money = 68
    total_bags = (total_money / 4) - (monday_bags + tuesday_bags)
    result = total_bags
    return result

print(solution())