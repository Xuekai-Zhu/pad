def solution():
    """Marco uses a fifth of an ounce of dry tea leaves to brew his morning cup of tea each day. He buys tea leaves in boxes of 28 ounces. How many weeks of daily tea does Marco get from a box?"""
    # Define the amount of tea used per day
    TEA_PER_DAY = 1/5

    # Define the size of a box of tea leaves
    BOX_SIZE = 28

    # Calculate the amount of tea used in a week
    tea_per_week = TEA_PER_DAY * 7

    # Calculate the number of weeks of tea per box
    weeks_per_box = BOX_SIZE / tea_per_week

    # Display the number of weeks of tea per box
    result = weeks_per_box
    return result

print(solution())