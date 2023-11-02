def solution():
    """Carlton wears an assortment of sweater vests and button-up shirts. He has twice as many sweater vests as button-up shirts and considers each unique combination of vest and shirt to be an outfit. He owns three button-up shirts. How many outfits does Carlton have?"""
    # Define the number of button-up shirts
    button_up_shirts = 3

    # Calculate the number of sweater vests
    sweater_vests = button_up_shirts * 2

    # Calculate the total number of possible outfits
    outfits = button_up_shirts * sweater_vests

    # return the result
    result = outfits
    return result

print(solution())