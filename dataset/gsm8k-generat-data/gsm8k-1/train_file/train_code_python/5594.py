def solution():
    """When Matty was born, the cost of a ticket to Mars was $1,000,000. The cost is halved every 10 years. How much will a ticket cost when Matty is 30?"""
    initial_price = 1000000
    time_passed = 30/10
    final_price = initial_price / (2**time_passed)
    result = final_price
    return result

print(solution())