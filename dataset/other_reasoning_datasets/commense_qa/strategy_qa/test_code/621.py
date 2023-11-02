def solution():
    # Define the Cookie Monster's appetite and the Keebler Company's product
    cookie_monster_appetite = "enormous"
    keebler_product = "cookies"
    # Check if the Cookie Monster would decline an offer of free Keebler products
    if keebler_product != cookie_monster_appetite:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())