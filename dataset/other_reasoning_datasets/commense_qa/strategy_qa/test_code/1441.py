def solution():
    # Define the last repainting year and the end of Trump's first term
    last_repaint_year = 2018
    trump_first_term_end = 2021
    # Calculate the number of years between the last repainting year and the end of Trump's first term
    years_since_last_repaint = trump_first_term_end - last_repaint_year
    # Check if that number is less than or equal to five
    if years_since_last_repaint <= 5:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())