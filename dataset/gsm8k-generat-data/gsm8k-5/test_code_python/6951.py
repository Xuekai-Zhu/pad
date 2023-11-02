def solution():
    # Let x be the amount of storage space on the second floor
    # The first floor contains twice as much space as the second floor, so the total storage space is 3x
    x = 5000 * 4  # The boxes fill one-quarter of the second floor, so x = 5000 * 4 = 20,000 square feet

    total_space = 3 * x
    used_space = x + 5000
    remaining_space = total_space - used_space
    result = remaining_space
    return result

print(solution())