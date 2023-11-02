def solution():
    """Patricia and Geoffrey went fishing to feed their group of campers. They caught an eight-pound trout, six two-pound bass, and two twelve-pound salmon. If each person will eat two pounds of fish, how many campers can they feed?"""
    # Calculate the total weight of all the fish caught
    total_weight = 8 + (6 * 2) + (2 * 12)

    # Calculate the number of campers they can feed
    num_campers = total_weight // 2

    # Display the number of campers they can feed
    result = num_campers
    return result

print(solution())