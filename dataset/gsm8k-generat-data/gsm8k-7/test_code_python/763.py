def solution():
    total_ribbon = 18
    num_gifts = 6
    ribbon_per_gift = 2

    # Calculate the total ribbon needed for all gifts
    total_ribbon_used = num_gifts * ribbon_per_gift

    # Calculate the amount of ribbon left
    ribbon_left = total_ribbon - total_ribbon_used
    result = ribbon_left
    return result

print(solution())