def solution():
    """Reuben opens a sandwich shop selling his namesake sandwich and pastrami sandwiches. Pastrami cost $2 more than the Reuben. He sells 10 Reubens and 5 Pastrami sandwiches and earns $55. How much does a pastrami sandwich cost?"""
    # Define the number of Reubens and Pastrami sandwiches sold
    reubens = 10
    pastramis = 5

    # Define the price difference between a Pastrami and a Reuben
    price_difference = 2

    # Define the total earnings
    total_earnings = 55

    # Calculate the cost of a Reuben sandwich
    reuben_cost = total_earnings / (reubens + (pastramis * (price_difference/2)))

    # Calculate the cost of a Pastrami sandwich
    pastrami_cost = reuben_cost + price_difference

    result = pastrami_cost
    return result

print(solution())