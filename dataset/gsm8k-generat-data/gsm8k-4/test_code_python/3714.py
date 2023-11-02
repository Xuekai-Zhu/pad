def solution():
    """Jacoby wants to save money for a trip to Brickville. He needs to have $5000 total to go on his trip. He works a job earning $20 per hour and works 10 hours. He then finds he can sell cookies for $4 each, and he sells 24 pieces of cookies. With the money he has so far, he buys a lottery ticket for $10 and wins $500. Finally, he gets $500 from both of his sisters as a gift. How much more, in dollars, does Jacob need to go to Brickville?"""
    # Define the cost of the trip
    TRIP_COST = 5000

    # Calculate Jacoby's earnings from his job
    job_earnings = 20 * 10

    # Calculate the earnings from selling cookies
    cookie_earnings = 4 * 24

    # Calculate the total amount of money Jacoby has so far
    total_money = job_earnings + cookie_earnings - 10 + 500 + 500

    # Calculate the amount of money Jacoby still needs to save
    remaining_money = TRIP_COST - total_money

    # return the result
    result = remaining_money
    return result

print(solution())