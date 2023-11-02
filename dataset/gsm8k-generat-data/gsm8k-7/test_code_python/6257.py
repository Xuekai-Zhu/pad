def solution():
    bags_morning = 3
    bags_afternoon = bags_morning * 3
    bags_evening = bags_morning * 2
    days_per_week = 7

    # Calculate the total number of bags of coffee beans used in a week
    total_bags_per_day = bags_morning + bags_afternoon + bags_evening
    total_bags_per_week = total_bags_per_day * days_per_week
    result = total_bags_per_week
    return result

print(solution())