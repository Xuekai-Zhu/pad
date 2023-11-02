def solution():
    # Calculate the total amount Toby gave to his brothers
    amount_to_brothers = (1/7) * 343 * 2  # Toby has 2 brothers

    # Calculate how much money is left for Toby
    left_for_Toby = 343 - amount_to_brothers
    result = left_for_Toby
    return result

print(solution())