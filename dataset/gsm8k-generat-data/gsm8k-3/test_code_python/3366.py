def solution():
    """Simon and Peter have a big stamp collection. Simon collects red stamps and Peter collects white stamps. Simon has 30 red stamps and Peter has 80 white stamps. If the red stamps are then sold for 50 cents each and the white stamps are sold for 20 cents each, what is the difference in the amount of money they make in dollars?"""
    # Define the prices of red and white stamps
    RED_PRICE = 0.5 # in dollars
    WHITE_PRICE = 0.2 # in dollars

    # Define the number of red and white stamps
    red_stamps = 30
    white_stamps = 80

    # Calculate the total amount of money made from red stamps
    red_money = red_stamps * RED_PRICE

    # Calculate the total amount of money made from white stamps
    white_money = white_stamps * WHITE_PRICE

    # Calculate the difference in the amount of money they make
    difference = red_money - white_money

    # Display the difference in dollars
    result = difference
    return result

print(solution())