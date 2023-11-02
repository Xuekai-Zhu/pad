def solution():
    full_year = 4 # Number of digits in "2022"
    happy_new_year = len("HAPPYNEWYEAR")  # Number of letters in "HAPPY NEW YEAR"
    extra_boxes = 50
    fireworks_per_box = 8
    fireworks_per_digit = 6
    fireworks_per_letter = 5

    # Calculate the number of fireworks for the full year display
    total_fireworks_year = full_year * fireworks_per_digit

    # Calculate the number of fireworks for the "HAPPY NEW YEAR" display
    total_fireworks_hny = happy_new_year * fireworks_per_letter

    # Calculate the number of fireworks in the extra boxes
    total_extra_fireworks = extra_boxes * fireworks_per_box

    # Calculate the grand total of all fireworks lit during the display
    grand_total = total_fireworks_year + total_fireworks_hny + total_extra_fireworks
    result = grand_total
    return result

print(solution())