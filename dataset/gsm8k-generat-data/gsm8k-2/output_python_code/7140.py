def solution():
    """Normally Ann can frost a cake in 5 minutes. However, today she has a sprained wrist and it takes her 8 minutes to frost a cake. How much longer would it take her to frost 10 cakes with her sprained wrist?"""
    normal_time_per_cake = 5
    injured_time_per_cake = 8
    extra_time_per_cake = injured_time_per_cake - normal_time_per_cake
    num_cakes = 10
    extra_time_total = extra_time_per_cake * num_cakes
    result = extra_time_total
    return result

print(solution())