def solution():
    """Droid owns a coffee shop. He uses 3 bags of coffee beans every morning, he uses triple that number in the afternoon than in the morning, and he uses twice the morning number in the evening. How many bags of coffee beans does he use every week?"""
    bags_per_morning = 3
    bags_per_afternoon = 3 * 3
    bags_per_evening = 3 * 2
    bags_per_day = bags_per_morning + bags_per_afternoon + bags_per_evening
    bags_per_week = bags_per_day * 7
    result = bags_per_week
    return result

print(solution())