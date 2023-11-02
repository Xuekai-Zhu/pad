def solution():
    # Define the initial variables
    total_peaches = 18
    ripe_peaches = 4
    unripe_peaches = total_peaches - ripe_peaches
    days = 5

    # Calculate the number of ripe peaches after five days
    ripe_peaches += (2 * days)
    ripe_peaches -= 3  # Subtract the 3 peaches that were eaten on the third day

    # Calculate the difference between ripe and unripe peaches
    difference = ripe_peaches - unripe_peaches
    result = difference
    return result

print(solution())