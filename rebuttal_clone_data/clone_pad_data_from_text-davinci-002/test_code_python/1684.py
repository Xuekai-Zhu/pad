def solution():
    total_bags_sold = 100
    bags_sold_week_1 = 15
    bags_sold_week_2 = 3 * bags_sold_week_1
    bags_sold_week_3 = (total_bags_sold - (bags_sold_week_1 + bags_sold_week_2)) / 2
    bags_sold_week_4 = bags_sold_week_3
    result = [bags_sold_week_3, bags_sold_week_4]
    
    return result

print(solution())