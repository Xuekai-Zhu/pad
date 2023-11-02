def solution():
    
    bags_per_morning = 3
    bags_per_afternoon = 3 * 3
    bags_per_evening = 3 * 2
    bags_per_day = bags_per_morning + bags_per_afternoon + bags_per_evening
    bags_per_week = bags_per_day * 7
    result = bags_per_week
    return result

print(solution())