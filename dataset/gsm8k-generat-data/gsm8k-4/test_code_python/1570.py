def solution():
    """Holly loves to drink chocolate milk. With breakfast, she drinks 8 ounces of chocolate milk before leaving for work. During her lunch break, she buys a new 64-ounce container of chocolate milk and then drinks 8 ounces of it. With dinner, she drinks another 8 ounces of chocolate milk. If she ends the day with 56 ounces of chocolate milk, how many ounces of chocolate milk did she begin the day with?"""
    # Calculate the total amount of chocolate milk Holly drinks during the day
    total_consumed = 8 + 8 + 8 + 64 - 8

    # Calculate the amount of chocolate milk Holly had at the beginning of the day
    starting_amount = total_consumed + 56

    # return the result
    result = starting_amount
    return result

print(solution())