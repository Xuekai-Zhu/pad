def solution():
    """Making an equal number of drums of paint each day, a paint mixer takes three days to make 18 drums of paint. How many days will it take for him to make 360 drums of paint?"""
    drums_per_day = 18 / 3
    total_drums = 360
    days_to_make = total_drums / drums_per_day
    result = days_to_make
    return result

print(solution())