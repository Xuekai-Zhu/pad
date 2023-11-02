def solution():
    """Sandra wants to buy some sweets. She saved $10 for this purpose. Her mother gave her an additional $4, and her father twice as much as her mother. One candy costs $0.5, and one jelly bean $0.2. She wants to buy 14 candies and 20 jelly beans. How much money will she be left with after the purchase?"""
    # Define the cost of one candy and one jelly bean
    CANDY_PRICE = 0.5
    JELLY_BEAN_PRICE = 0.2

    # Calculate Sandra's total savings
    sandra_savings = 10 + 4 + 8  # Sandra's savings + mother's gift + father's gift

    # Calculate the total cost of the candies and jelly beans
    total_cost = 14 * CANDY_PRICE + 20 * JELLY_BEAN_PRICE

    # Calculate the amount of money Sandra will be left with
    money_left = sandra_savings - total_cost

    # Display the amount of money Sandra will be left with
    result = money_left
    return result

print(solution())