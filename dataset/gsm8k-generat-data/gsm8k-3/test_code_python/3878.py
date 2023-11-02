def solution():
    """During a fundraiser, each of the 20 members of a group sold candy bars which costs $0.50 each. If each member sold an average of 8 candy bars, how much money did they earn from their candy bars sales, in dollars?"""
    # Define the number of members, cost per candy bar, and average number of candy bars sold per member
    NUM_MEMBERS = 20
    CANDY_BAR_COST = 0.5
    AVG_CANDY_BARS_SOLD = 8

    # Calculate the total number of candy bars sold
    total_candy_bars_sold = NUM_MEMBERS * AVG_CANDY_BARS_SOLD

    # Calculate the total earnings from candy bar sales
    total_earnings = total_candy_bars_sold * CANDY_BAR_COST

    # Display the total earnings
    result = total_earnings
    return result

print(solution())