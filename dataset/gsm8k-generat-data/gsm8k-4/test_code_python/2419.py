def solution():
    """A bear is hunting for her cubs and herself. She needs 210 pounds of meat in a week. Each cub needs 35 pounds a week and she has 4 cubs. She hunts rabbits, which are five pounds each. If she hunts daily, how many rabbits does she need to catch each day?"""
    # Define the total amount of meat needed in a week
    total_meat = 210

    # Define the amount of meat needed for the cubs
    cub_meat = 35 * 4

    # Calculate the amount of meat needed for the bear
    bear_meat = total_meat - cub_meat

    # Calculate the number of rabbits needed to reach the required amount of meat, assuming she hunts daily
    rabbits_needed = (bear_meat / 5) / 7

    # Round up to the nearest whole number of rabbits
    rabbits_per_day = math.ceil(rabbits_needed)

    # Return the result
    result = rabbits_per_day
    return result

print(solution())