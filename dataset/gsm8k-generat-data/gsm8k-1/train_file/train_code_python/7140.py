def solution():
    """Normally Ann can frost a cake in 5 minutes. However, today she has a sprained wrist and it takes her 8 minutes to frost a cake. How much longer would it take her to frost 10 cakes with her sprained wrist?"""
    normal_time = 5
    sprained_time = 8
    time_difference = sprained_time - normal_time
    cakes_to_frost = 10
    extra_time = time_difference * cakes_to_frost
    result = extra_time
    return result

print(solution())