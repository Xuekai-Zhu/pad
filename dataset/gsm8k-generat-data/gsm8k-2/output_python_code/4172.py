def solution():
    """Jack is making barbecue sauce. He uses 3 cups of ketchup, 1 cup of vinegar and 1 cup of honey. If each burger takes 1/4 cup of sauce and each pulled pork sandwich takes 1/6 cup, how many burgers can Jack make if he makes 18 pulled pork sandwiches?"""
    ketchup_cups = 3
    vinegar_cups = 1
    honey_cups = 1
    sauce_cups = ketchup_cups + vinegar_cups + honey_cups
    pulled_pork_sandwiches = 18
    pulled_pork_sauce_cups = pulled_pork_sandwiches * (1/6)
    total_sauce_cups = sauce_cups + pulled_pork_sauce_cups
    burgers = total_sauce_cups / (1/4)
    result = int(burgers)
    return result

print(solution())