def solution():
    """Anna's mom gave her $10.00 to buy anything she wanted from the candy store. Anna bought 3 packs of chewing gum for $1.00 each, 5 chocolate bars at $1 each and 2 large candy canes for $0.50 each. How much money did Anna have left?"""
    # Define the initial amount of money Anna had
    initial_money = 10.00

    # Calculate the total cost of Anna's candy purchases
    total_cost = (3 * 1.00) + (5 * 1.00) + (2 * 0.50)

    # Calculate the amount of money Anna had left
    money_left = initial_money - total_cost

    # return the result
    result = money_left
    return result

print(solution())