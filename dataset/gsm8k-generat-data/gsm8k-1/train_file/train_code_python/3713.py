def solution():
    """Jacoby wants to save money for a trip to Brickville. He needs to have $5000 total to go on his trip. He works a job earning $20 per hour and works 10 hours. He then finds he can sell cookies for $4 each, and he sells 24 pieces of cookies. With the money he has so far, he buys a lottery ticket for $10 and wins $500. Finally, he gets $500 from both of his sisters as a gift. How much more, in dollars, does Jacob need to go to Brickville?"""
    total_needed = 5000
    job_earnings = 20 * 10
    cookie_sales = 24 * 4
    lottery_winnings = 500
    sister_gifts = 1000
    total_money = job_earnings + cookie_sales + lottery_winnings + sister_gifts
    still_needed = total_needed - total_money
    result = still_needed
    return result

print(solution())