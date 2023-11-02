def solution():
    """When Matty was born, the cost of a ticket to Mars was $1,000,000. The cost is halved every 10 years. How much will a ticket cost when Matty is 30?"""
    # Define the initial ticket price and the number of years for which it halves
    ticket_price = 1000000
    halving_years = 10

    # Calculate the number of times the price is halved by the time Matty is 30
    years_passed = 30
    halvings = years_passed // halving_years

    # Calculate the final ticket price
    final_price = ticket_price / (2 ** halvings)

    # Return the final price
    result = final_price
    return result

print(solution())