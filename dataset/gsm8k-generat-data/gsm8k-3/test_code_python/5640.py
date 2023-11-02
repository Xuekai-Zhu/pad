def solution():
    """Phantom's mom gave him $50 to buy printer-inks. At the store, he bought two black printer inks which cost $11 each, three red printer inks which cost $15 each, and two yellow printer inks which cost $13 each. Phantom found out that his money is not enough to buy all the printer inks. How much more money should he ask his mom to be able to buy the printer inks?"""
    # Define the prices of each color of printer ink
    BLACK_PRICE = 11
    RED_PRICE = 15
    YELLOW_PRICE = 13

    # Define the quantities of each color of printer ink purchased
    black_inks = 2
    red_inks = 3
    yellow_inks = 2

    # Calculate the total cost of the black inks
    black_cost = black_inks * BLACK_PRICE

    # Calculate the total cost of the red inks
    red_cost = red_inks * RED_PRICE

    # Calculate the total cost of the yellow inks
    yellow_cost = yellow_inks * YELLOW_PRICE

    # Calculate the total cost of all the inks purchased
    total_cost = black_cost + red_cost + yellow_cost

    # Calculate the amount of money Phantom needs to ask his mom for
    additional_cost = total_cost - 50

    # Display the additional cost
    result = additional_cost
    return result

print(solution())