def solution():
    # Calculate the total demerits Andy has already received
    demerits_so_far = (2 * 6) + 15  # 2 demerits per instance for being late 6 times, 15 demerits for inappropriate joke

    # Calculate the remaining demerits Andy can receive before getting fired
    remaining_demerits = 50 - demerits_so_far
    result = remaining_demerits
    return result

print(solution())