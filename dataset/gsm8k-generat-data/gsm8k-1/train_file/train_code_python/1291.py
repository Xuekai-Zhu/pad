def solution():
    """A town is holding a fireworks display for New Year’s Eve. They light enough fireworks to show the full year then light enough fireworks to write “HAPPY NEW YEAR” in the sky. They then light another 50 boxes of fireworks as part of the display. Each box of fireworks contains 8 fireworks. If it takes 6 fireworks to display a number and 5 fireworks to display a letter, how many fireworks are lit during the display?"""
    year_fireworks = 4*6  # 4 digits in a year, each requires 6 fireworks
    letters_fireworks = 12*5  # "HAPPY NEW YEAR" has 12 letters, each requires 5 fireworks
    extra_fireworks = 50*8  # 50 boxes of fireworks, each box contains 8 fireworks
    total_fireworks = year_fireworks + letters_fireworks + extra_fireworks
    result = total_fireworks
    return result

print(solution())