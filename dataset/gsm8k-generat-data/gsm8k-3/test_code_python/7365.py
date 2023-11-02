def solution():
    """Frank and Bill have $42 and they bought 3 large pizzas with the money. Each pizza cost $11 and Frank paid for all three pizzas. Frank gave the rest of his money to Bill. If Bill had $30 already, how much money does Bill have now?"""
    # Calculate the total cost of the pizzas
    pizza_cost = 11 * 3

    # Calculate how much Frank gave to Bill
    frank_gave = 42 - pizza_cost

    # Add Frank's remaining money to what Bill already had
    bill_total = frank_gave + 30

    # Display how much money Bill now has
    result = bill_total
    return result

print(solution())