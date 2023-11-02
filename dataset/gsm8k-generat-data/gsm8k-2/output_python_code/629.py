def solution():
    """On her birthday, Avianna bought red candles and blue candles in the ratio of 5:3. If Avianna had 45 red candles on her birthday, how many blue candles did she have?"""
    red_ratio = 5
    blue_ratio = 3
    total_ratio = red_ratio + blue_ratio
    red_candles = 45
    red_unit = red_candles / red_ratio
    blue_unit = red_unit * blue_ratio
    total_blue = blue_unit * total_ratio - red_candles
    result = total_blue
    return result

print(solution())