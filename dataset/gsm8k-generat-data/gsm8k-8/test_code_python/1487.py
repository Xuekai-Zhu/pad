def solution():
    # Calculate the rate of egg laying per hen per day
    eggs_per_hen_per_day = 80 / (10*10)

    # Calculate the total number of hens
    total_hens = 10 + 15

    # Calculate the total number of eggs in 15 days
    total_eggs = total_hens * eggs_per_hen_per_day * 15
    result = total_eggs
    return result

print(solution())