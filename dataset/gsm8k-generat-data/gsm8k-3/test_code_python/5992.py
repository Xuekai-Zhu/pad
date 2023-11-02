def solution():
    """Bill's roof can bear 500 pounds of weight. If 100 leaves fall on his roof every day, and 1000 leaves weighs 1 pound, how many days will it take for his roof to collapse?"""
    # Define the weight of 1000 leaves
    LEAVES_WEIGHT = 1

    # Define the weight capacity of Bill's roof
    ROOF_CAPACITY = 500

    # Define the number of leaves that fall on Bill's roof every day
    DAILY_LEAVES = 100

    # Calculate the weight of leaves that fall on Bill's roof every day
    DAILY_WEIGHT = DAILY_LEAVES / 1000 * LEAVES_WEIGHT

    # Calculate the number of days it will take for Bill's roof to collapse
    days = ROOF_CAPACITY / DAILY_WEIGHT

    # Display the number of days
    result = days
    return result

print(solution())