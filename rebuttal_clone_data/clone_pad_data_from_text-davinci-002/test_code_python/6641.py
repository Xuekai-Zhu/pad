def solution():
    previous_spider_weight = 6.4
    current_spider_weight = previous_spider_weight * 2.5
    leg_area = .5
    total_pressure = current_spider_weight / leg_area
    result = total_pressure
    
    return result

print(solution())