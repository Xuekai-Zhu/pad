def solution():
    """A town is holding a fireworks display for New Year’s Eve. They light enough fireworks to show the full year then light enough fireworks to write “HAPPY NEW YEAR” in the sky. They then light another 50 boxes of fireworks as part of the display. Each box of fireworks contains 8 fireworks. If it takes 6 fireworks to display a number and 5 fireworks to display a letter, how many fireworks are lit during the display?"""
    # Define the number of fireworks needed for each digit of the year
    YEAR_DIGITS = 4

    # Define the number of fireworks needed for each letter in "HAPPY NEW YEAR"
    LETTER_FIREWORKS = [6, 5, 7, 7, 4, 5, 4, 5, 4, 7, 5]

    # Calculate the total number of fireworks needed for the year
    year_fireworks = YEAR_DIGITS * 6

    # Calculate the total number of fireworks needed for the letters
    letter_fireworks = sum(LETTER_FIREWORKS)

    # Calculate the total number of fireworks needed for the display
    total_fireworks = year_fireworks + letter_fireworks + (50 * 8)

    # Display the total number of fireworks
    result = total_fireworks
    return result

print(solution())