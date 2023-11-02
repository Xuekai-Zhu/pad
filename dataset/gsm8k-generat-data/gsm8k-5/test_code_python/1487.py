def solution():
    # Calculate the average number of eggs laid per hen per day
    eggs_per_hen_per_day = 80 / (10 * 10)  # 80 eggs in 10 days, 10 hens

    # Calculate the total number of eggs laid by 25 hens in 15 days
    total_eggs = (25 * eggs_per_hen_per_day * 15)

    result = total_eggs
    return result

print(solution())