def solution():
    """When Diane turns 30, she will be half the age of Alex and twice as old as Allison. Diane is 16 years old now. What is the sum of the ages of Alex and Allison now?"""
    diane_current_age = 16
    diane_future_age = 30
    alex_future_age = diane_future_age * 2
    allison_future_age = diane_future_age / 2
    sum_alex_allison = (alex_future_age - diane_future_age) + (allison_future_age - diane_future_age)
    sum_alex_allison_current = sum_alex_allison - (diane_future_age - diane_current_age)
    result = sum_alex_allison_current
    return result

print(solution())