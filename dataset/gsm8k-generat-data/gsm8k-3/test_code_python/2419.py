def solution():
    """A bear is hunting for her cubs and herself. She needs 210 pounds of meat in a week. Each cub needs 35 pounds a week and she has 4 cubs. She hunts rabbits, which are five pounds each. If she hunts daily, how many rabbits does she need to catch each day?"""

    # Calculate the total meat needed for the cubs
    cubs_meat = 4 * 35

    # Calculate the meat needed for the bear
    bear_meat = 210 - cubs_meat

    # Calculate the number of rabbits needed per day
    rabbits_per_day = bear_meat / 5 / 7

    # Display the number of rabbits needed per day
    result = rabbits_per_day
    return result

print(solution())