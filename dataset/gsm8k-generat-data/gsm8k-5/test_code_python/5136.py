def solution():
    # Calculate the number of flowers on each hibiscus plant
    flowers_first = 2
    flowers_second = 2 * flowers_first
    flowers_third = 4 * flowers_second

    # Calculate the total number of blossoms
    total_blossoms = flowers_first + flowers_second + flowers_third
    result = total_blossoms
    return result

print(solution())