def solution():
    # Calculate the total weight of dog food consumed by both dogs in a day
    weight_per_day = (1/4) * 6 * 2 * 2  # 1/4 pound per cup, 6 cups per dog, 2 dogs, twice per day

    # Calculate the total weight of dog food consumed in a month
    weight_per_month = weight_per_day * 30  # assuming there are 30 days in a month

    # Calculate the number of 20-pound bags needed
    bags_needed = weight_per_month / 20

    result = bags_needed
    return result

print(solution())