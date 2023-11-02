def solution():
    """Emily can peel 6 shrimp a minute and saute 30 shrimp in 10 minutes. How long will it take her to peel and cook 90 shrimp?"""
    shrimp_per_minute = 6
    saute_time = 10
    saute_amount = 30
    total_shrimp = 90
    peel_time = (total_shrimp - saute_amount) / shrimp_per_minute
    total_time = peel_time + saute_time
    result = total_time
    return result

print(solution())