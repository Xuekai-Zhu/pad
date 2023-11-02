def solution():
    """Carlton wears an assortment of sweater vests and button-up shirts. He has twice as many sweater vests as button-up shirts and considers each unique combination of vest and shirt to be an outfit. He owns three button-up shirts. How many outfits does Carlton have?"""
    button_up_shirts = 3
    sweater_vests = button_up_shirts * 2
    outfits = button_up_shirts * sweater_vests
    result = outfits
    return result

print(solution())