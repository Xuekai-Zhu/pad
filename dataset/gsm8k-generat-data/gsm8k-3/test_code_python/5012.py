def solution():
    """Carlton wears an assortment of sweater vests and button-up shirts. He has twice as many sweater vests as button-up shirts and considers each unique combination of vest and shirt to be an outfit. He owns three button-up shirts. How many outfits does Carlton have?"""
    # Number of button-up shirts
    num_button_up = 3

    # Number of sweater vests
    num_vests = 2 * num_button_up

    # Total number of outfits
    total_outfits = num_button_up * num_vests

    # Display the total number of outfits
    result = total_outfits
    return result

print(solution())