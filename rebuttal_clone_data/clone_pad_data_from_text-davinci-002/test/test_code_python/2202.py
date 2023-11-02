def solution():
    bags_collected_by_gina = 2
    bags_collected_by_neighborhood = bags_collected_by_gina * 82
    pounds_per_bag = 4
    total_pounds = pounds_per_bag * (bags_collected_by_gina + bags_collected_by_neighborhood)
    result = total_pounds
    
    return result

print(solution())