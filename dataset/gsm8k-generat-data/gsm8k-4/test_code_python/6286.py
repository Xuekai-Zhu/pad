def solution():
    """3000 bees hatch from the queen's eggs every day. If a queen loses 900 bees every day, how many total bees are in the hive (including the queen) at the end of 7 days if at the beginning the queen had 12500 bees?"""
    # Define the initial number of bees
    initial_bees = 12500

    # Define the number of bees hatching and losing each day
    hatching_bees = 3000
    losing_bees = 900

    # Calculate the number of bees after 7 days
    total_bees = initial_bees + (hatching_bees-losing_bees) * 7

    # return the result
    result = total_bees
    return result

print(solution())