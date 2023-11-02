def solution():
    """Jacoby wants to save money for a trip to Brickville. He needs to have $5000 total to go on his trip. He works a job earning $20 per hour and works 10 hours. He then finds he can sell cookies for $4 each, and he sells 24 pieces of cookies. With the money he has so far, he buys a lottery ticket for $10 and wins $500. Finally, he gets $500 from both of his sisters as a gift. How much more, in dollars, does Jacob need to go to Brickville?"""
    total_money = 0
    job_money = 20 * 10
    cookie_money = 4 * 24
    lottery_money = 500 - 10
    gift_money = 500 * 2
    total_money += job_money + cookie_money + lottery_money + gift_money
    remaining_money = 5000 - total_money
    result = remaining_money
    return result

print(solution())