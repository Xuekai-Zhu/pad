def solution():
    # Calculate the total ounces of cleaner used in 30 minutes
    ounces_per_min = [2] * 15 + [3] * 10 + [4] * 5  # list of ounces per minute for each segment of time
    total_ounces = sum(ounces_per_min)
    result = total_ounces
    return result

print(solution())