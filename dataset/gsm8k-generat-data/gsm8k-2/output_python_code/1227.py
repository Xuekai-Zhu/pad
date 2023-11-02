def solution():
    """Making an equal number of drums of paint each day, a paint mixer takes three days to make 18 drums of paint. How many days will it take for him to make 360 drums of paint?"""
    drums_per_day = 18 / 3 # The mixer can make 6 drums of paint in one day
    total_drums = 360
    days_needed = total_drums / drums_per_day
    result = days_needed
    return result

print(solution())