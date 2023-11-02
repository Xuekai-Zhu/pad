def solution():
    num_brown1 = 9
    num_brown2 = 12
    num_brown3 = 8
    num_brown4 = 8
    num_brown5 = 3
    num_bags = 5

    # Calculate the total number of brown M&M's set aside
    total_brown = num_brown1 + num_brown2 + num_brown3 + num_brown4 + num_brown5

    # Calculate the total number of M&M's in all bags
    total_mm = (num_bags * 50) - total_brown

    # Calculate the average number of brown M&M's in a bag
    avg_brown = total_brown / num_bags
    result = avg_brown
    return result

print(solution())