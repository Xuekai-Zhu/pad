def solution():
    """On her birthday, Avianna bought red candles and blue candles in the ratio of 5:3. If Avianna had 45 red candles on her birthday, how many blue candles did she have?"""
    # Define the ratio of red candles to blue candles
    red_blue_ratio = 5/3

    # Calculate the number of blue candles for every 5 red candles
    blue_per_five_red = 3 / 5

    # Calculate the total number of red and blue candles
    total_candles = 45 / blue_per_five_red

    # Calculate the number of blue candles
    blue_candles = total_candles - 45

    result = blue_candles
    return result

print(solution())