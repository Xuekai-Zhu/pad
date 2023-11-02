def solution():
    # Calculate the number of fireworks lit to show the full year
    year_fireworks = 4 * 6  # 4 digits in the year, and it takes 6 fireworks to display a digit

    # Calculate the number of fireworks lit to write "HAPPY NEW YEAR"
    letter_fireworks = 12 * 5  # there are 12 letters in the phrase, and it takes 5 fireworks to display a letter

    # Calculate the total number of fireworks lit for the display
    total_fireworks = year_fireworks + letter_fireworks + 50*8  # 50 boxes of 8 fireworks each

    result = total_fireworks
    return result

print(solution())