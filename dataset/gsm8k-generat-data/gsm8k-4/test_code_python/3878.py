def solution():
    """During a fundraiser, each of the 20 members of a group sold candy bars which costs $0.50 each. If each member sold an average of 8 candy bars, how much money did they earn from their candy bars sales, in dollars?"""
    # Define the number of members in the group
    num_members = 20

    # Define the price of each candy bar
    candy_bar_price = 0.5

    # Define the number of candy bars sold by each member
    num_candy_bars = 8

    # Calculate the total number of candy bars sold
    total_candy_bars = num_members * num_candy_bars

    # Calculate the total earnings from candy bar sales
    total_earnings = total_candy_bars * candy_bar_price

    # return the result
    result = total_earnings
    return result

print(solution())