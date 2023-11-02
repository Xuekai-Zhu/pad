def solution():
    """A bowl of fruit holds 18 peaches. Four of the peaches are ripe and two more ripen every day, but on the third day three are eaten. How many more ripe peaches than unripe peaches are in the bowl after five days?"""
    # Define the number of ripe peaches to start
    ripe_peaches = 4

    # Define the number of unripe peaches to start
    unripe_peaches = 18 - ripe_peaches

    # Calculate the number of ripe peaches after 5 days
    ripe_peaches += 2 * 5

    # Subtract the 3 peaches that were eaten on the third day
    ripe_peaches -= 3

    # Calculate the number of unripe peaches after 5 days
    unripe_peaches -= 2 * 2

    # Calculate the difference between the number of ripe and unripe peaches
    difference = ripe_peaches - unripe_peaches

    # Display the difference between the number of ripe and unripe peaches
    result = difference
    return result

print(solution())