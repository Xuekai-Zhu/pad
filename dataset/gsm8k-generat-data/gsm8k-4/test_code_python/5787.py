def solution():
    """Apples used to cost $1.6 per pound. The price got raised 25%. How much does it cost to buy 2 pounds of apples for each person in a 4 member family?"""
    # Define the initial price and the percentage increase
    INITIAL_PRICE = 1.6
    PERCENTAGE_INCREASE = 0.25

    # Calculate the new price after the percentage increase
    new_price = INITIAL_PRICE * (1 + PERCENTAGE_INCREASE)

    # Calculate the cost of 2 pounds of apples for each person in a 4 member family
    cost = 2 * new_price * 4

    result = cost
    return result

print(solution())