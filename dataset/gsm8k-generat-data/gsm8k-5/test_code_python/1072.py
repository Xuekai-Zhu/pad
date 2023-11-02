def solution():
    shirts_type1 = 200  # Large department store ordered 200 of first type of shirts
    shirts_type2 = 200  # Large department store ordered 200 of second type of shirts
    buttons_type1 = 3  # First type of shirt has 3 buttons
    buttons_type2 = 5  # Second type of shirt has 5 buttons

    # Calculate the total number of buttons used to manufacture all shirts
    total_buttons = (shirts_type1 * buttons_type1) + (shirts_type2 * buttons_type2)
    result = total_buttons
    return result

print(solution())