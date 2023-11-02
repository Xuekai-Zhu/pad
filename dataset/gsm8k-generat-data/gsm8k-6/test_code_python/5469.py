def solution():
    # Calculate the total number of brown M&M's set aside by Robby
    total_brown_MMs = 9 + 12 + 8 + 8 + 3  # number of brown M&M's set aside on each bag
    num_bags = 5  # total number of bags
    avg_brown_MMs = total_brown_MMs / num_bags  # average number of brown M&M's per bag
    result = avg_brown_MMs
    return result

print(solution())