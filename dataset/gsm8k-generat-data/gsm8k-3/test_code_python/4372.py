def solution():
    """Cory has $20.00 and she wants to buy two packs of candies that cost $49.00 each. How much money does Cory need so she will be able to buy the pack of candies?"""
    # Define the cost of each pack of candies
    CANDY_PRICE = 49

    # Define Cory's initial amount of money
    initial_money = 20

    # Calculate the total cost of the two packs of candies
    total_cost = CANDY_PRICE * 2

    # Calculate how much more money Cory needs to buy the candies
    additional_money = total_cost - initial_money

    # Display how much more money Cory needs
    result = additional_money
    return result

print(solution())