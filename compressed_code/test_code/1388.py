def solution():
    
    total_candies = 90
    lollipops = total_candies // 3
    candy_canes = total_candies - lollipops
    boys = lollipops // 3
    girls = candy_canes // 2
    total_children = boys + girls
    result = total_children
    return result

print(solution())