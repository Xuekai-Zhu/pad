def solution():
    # Calculate the total weight of fish caught by James
    salmon_weight = 200 * 1.5  # salmon weight is 50% more than trout weight
    tuna_weight = 2 * 200  # tuna weight is twice the trout weight
    total_weight = 200 + salmon_weight + tuna_weight
    result = total_weight
    return result

print(solution())