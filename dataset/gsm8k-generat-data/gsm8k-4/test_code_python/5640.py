def solution():
    """Phantom's mom gave him $50 to buy printer-inks. At the store, he bought two black printer inks which cost $11 each, three red printer inks which cost $15 each, and two yellow printer inks which cost $13 each. Phantom found out that his money is not enough to buy all the printer inks. How much more money should he ask his mom to be able to buy the printer inks?"""
    # Define the amount of money Phantom has
    money_available = 50

    # Define the cost of each type of ink
    black_ink_cost = 11
    red_ink_cost = 15
    yellow_ink_cost = 13

    # Define the number of inks Phantom bought for each color
    black_ink_count = 2
    red_ink_count = 3
    yellow_ink_count = 2

    # Calculate the total cost of the inks Phantom bought
    total_cost = black_ink_count*black_ink_cost + red_ink_count*red_ink_cost + yellow_ink_count*yellow_ink_cost

    # Calculate the amount of money Phantom should ask his mom for
    additional_money = total_cost - money_available

    # return the result
    result = additional_money
    return result

print(solution())