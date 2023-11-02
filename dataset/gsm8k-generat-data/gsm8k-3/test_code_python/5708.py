def solution():
    """Reuben opens a sandwich shop selling his namesake sandwich and pastrami sandwiches. Pastrami cost $2 more than the Reuben. He sells 10 Reubens and 5 Pastrami sandwiches and earns $55. How much does a pastrami sandwich cost?"""
    # Define the price of a Reuben sandwich
    REUBEN_PRICE = x

    # Define the price difference between a Reuben and a Pastrami
    PRICE_DIFFERENCE = 2

    # Calculate the price of a Pastrami sandwich
    pastrami_price = REUBEN_PRICE + PRICE_DIFFERENCE

    # Calculate the total earnings from Reubens and Pastramis
    total_earnings = 10 * REUBEN_PRICE + 5 * pastrami_price

    # Check if the total earnings match the given amount of $55
    if total_earnings == 55:
        result = pastrami_price
    else:
        result = "Unable to calculate pastrami price"

    return result

print(solution())