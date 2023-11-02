def solution():
    """Simon and Peter have a big stamp collection. Simon collects red stamps and Peter collects white stamps. Simon has 30 red stamps and Peter has 80 white stamps. If the red stamps are then sold for 50 cents each and the white stamps are sold for 20 cents each, what is the difference in the amount of money they make in dollars?"""
    # Define the number of red and white stamps
    num_red = 30
    num_white = 80

    # Calculate the total earnings for selling the red stamps
    earnings_red = num_red * 0.5

    # Calculate the total earnings for selling the white stamps
    earnings_white = num_white * 0.2

    # Calculate the difference in earnings
    difference = earnings_red - earnings_white

    # Convert the difference to dollars
    difference_dollars = difference / 100

    result = difference_dollars
    return result

print(solution())