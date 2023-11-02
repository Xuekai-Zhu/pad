def solution():
    # Calculate the number of fresh peaches
    fresh_peaches = int(0.6 * 250)

    # Calculate the number of peaches after throwing away 15 small ones
    remaining_peaches = fresh_peaches - 15
    result = remaining_peaches
    return result

print(solution())