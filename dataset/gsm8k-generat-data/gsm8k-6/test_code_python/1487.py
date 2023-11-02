def solution():
    # Calculate the rate of egg-laying per hen per day
    rate = 80 / (10*10)  # 80 eggs in 10 days with 10 hens

    # Calculate the total number of hens
    total_hens = 10 + 15

    # Calculate the total number of eggs laid in 15 days
    total_eggs = rate * total_hens * 15

    result = total_eggs
    return result

print(solution())