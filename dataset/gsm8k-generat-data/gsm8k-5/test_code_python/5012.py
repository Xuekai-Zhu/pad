def solution():
    button_up_shirts = 3  # Carlton has three button-up shirts
    sweater_vests = 2 * button_up_shirts  # Carlton has twice as many sweater vests as button-up shirts
    outfits = button_up_shirts * sweater_vests  # Each unique combination of a button-up shirt and sweater vest is an outfit
    result = outfits
    return result

print(solution())