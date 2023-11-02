def solution():
    """Sunny bakes 8 cakes. Then she gives away 2 cakes. Sunny wants to put candles on the remaining cakes. If she puts 6 candles on each cake, how many candles will she use in total?"""
    # Define the initial number of cakes
    initial_cakes = 8

    # Define the number of cakes given away
    given_cakes = 2

    # Calculate the remaining cakes
    remaining_cakes = initial_cakes - given_cakes

    # Calculate the total number of candles used
    total_candles = remaining_cakes * 6

    # return the result
    result = total_candles
    return result

print(solution())