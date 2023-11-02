def solution():
    
    monday_bags = 5
    tuesday_bags = 3
    total_bags = monday_bags + tuesday_bags
    total_money = 68
    total_money_so_far = total_bags * 4
    wednesday_money = total_money - total_money_so_far
    wednesday_bags = wednesday_money / 4
    result = wednesday_bags
    return result

print(solution())