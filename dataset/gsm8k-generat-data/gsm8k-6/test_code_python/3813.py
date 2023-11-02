def solution():
    # Calculate the number of candles Carmen burns in 8 nights if she burns it for 1 hour per night
    candles_1_hour = 8  

    # Calculate the number of candles Carmen will use in 24 nights if she burns it for 2 hours per night
    candles_2_hours = 24//2  

    result = candles_1_hour + candles_2_hours
    return result

print(solution())