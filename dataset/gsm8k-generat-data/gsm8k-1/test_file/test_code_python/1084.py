def solution():
    """There are 6 periods in the day for a normal student but John has to take 2 extra classes. Each class is 40 minutes long. He goes to class for 5 days a week. He then spends 1/16 of his weekly minutes each on Saturday and Sunday as extra learning time. How many hours a week does he spend learning?"""
    normal_periods = 6
    extra_periods = 2
    period_length = 40
    school_days = 5
    learning_days = 2
    extra_learning_ratio = 1/16
    
    total_periods = normal_periods + extra_periods
    total_period_length = total_periods * period_length
    total_learning_minutes = (total_period_length * school_days) + (extra_learning_ratio * total_period_length * learning_days)
    total_learning_hours = total_learning_minutes / 60
    result = total_learning_hours
    return result

print(solution())