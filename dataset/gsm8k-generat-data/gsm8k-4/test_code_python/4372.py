def solution():
    """Cory has $20.00 and she wants to buy two packs of candies that cost $49.00 each. How much money does Cory need so she will be able to buy the pack of candies?"""
    # Define the initial amount of money Cory has
    initial_money = 20

    # Define the cost of two packs of candies
    candy_cost = 49 * 2

    # Calculate the total amount of money Cory needs to buy the candies
    total_cost = candy_cost - initial_money

    # return the result
    result = total_cost
    return result

print(solution())