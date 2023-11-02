def solution():
    """On her birthday, Avianna bought red candles and blue candles in the ratio of 5:3. If Avianna had 45 red candles on her birthday, how many blue candles did she have?"""
    # Define the ratio of red candles to blue candles
    red_blue_ratio = 5/3

    # Define the number of red candles Avianna had
    red_candles = 45

    # Calculate the number of blue candles Avianna had
    blue_candles = red_candles/red_blue_ratio * (1 - red_blue_ratio)

    # Display the number of blue candles
    result = blue_candles
    return result

print(solution())