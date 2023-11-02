def solution():
    fireworks_per_number = 6  # It takes 6 fireworks to display a number
    fireworks_per_letter = 5  # It takes 5 fireworks to display a letter
    boxes_of_fireworks = 50  # There are 50 boxes of fireworks in the display
    fireworks_per_box = 8  # Each box of fireworks contains 8 fireworks

    # Calculate the number of fireworks needed to display the full year
    fireworks_for_year = fireworks_per_number * 4  # There are 4 digits in a year

    # Calculate the number of fireworks needed to display "HAPPY NEW YEAR"
    fireworks_for_message = fireworks_per_letter * len("HAPPY NEW YEAR")

    # Calculate the total number of fireworks needed for the display
    total_fireworks = fireworks_for_year + fireworks_for_message + (boxes_of_fireworks * fireworks_per_box)
    result = total_fireworks
    return result

print(solution())