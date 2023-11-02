def solution():
    """Jacoby wants to save money for a trip to Brickville. He needs to have $5000 total to go on his trip. He works a job earning $20 per hour and works 10 hours. He then finds he can sell cookies for $4 each, and he sells 24 pieces of cookies. With the money he has so far, he buys a lottery ticket for $10 and wins $500. Finally, he gets $500 from both of his sisters as a gift. How much more, in dollars, does Jacob need to go to Brickville?"""
    # Calculate Jacoby's earnings from his job
    job_earnings = 20 * 10

    # Calculate Jacoby's earnings from selling cookies
    cookie_earnings = 4 * 24

    # Calculate Jacoby's total earnings
    total_earnings = job_earnings + cookie_earnings + 500 + 1000

    # Calculate the amount Jacoby still needs to save for his trip
    amount_left = 5000 - total_earnings

    # Display the amount Jacoby still needs to save
    result = amount_left
    return result

print(solution())