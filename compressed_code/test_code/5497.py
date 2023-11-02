def solution():
    
    max_weight = 13500
    yesterday_weight = 100 * 100
    today_weight = 10 * 60 + 50 * 50
    current_weight = yesterday_weight + today_weight
    remaining_weight = max_weight - current_weight
    bags_weight = 40
    bags_count = remaining_weight // bags_weight
    result = bags_count
    return result

print(solution())