def solution():
    """Sunny bakes 8 cakes. Then she gives away 2 cakes. Sunny wants to put candles on the remaining cakes. If she puts 6 candles on each cake, how many candles will she use in total?"""
    # Define the number of cakes baked and given away
    cakes_baked = 8
    cakes_given_away = 2

    # Calculate the number of remaining cakes
    remaining_cakes = cakes_baked - cakes_given_away

    # Calculate the total number of candles used
    total_candles = remaining_cakes * 6

    # Display the total number of candles used
    result = total_candles
    return result

print(solution())