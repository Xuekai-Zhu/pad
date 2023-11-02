def solution():
    """Tom decides to take 10 dance lessons that cost $10 each, but he gets two of them for free. How much does he pay?"""
    # Define the price per dance lesson and the number of lessons taken
    PRICE_PER_LESSON = 10
    NUM_LESSONS = 10

    # Calculate the total cost before the discount
    total_cost = PRICE_PER_LESSON * NUM_LESSONS

    # Calculate the cost after the discount
    discounted_cost = total_cost - (PRICE_PER_LESSON * 2)

    # return the result
    result = discounted_cost
    return result

print(solution())