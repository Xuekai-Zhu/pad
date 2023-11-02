def solution():
    """Erin has 7 lollipops. Her mother gives Erin another 10 lollipops. If Erin gives 3 of her lollipops to Ella, how many lollipops does she have left?"""
    initial_lollipops = 7
    lollipops_from_mom = 10
    lollipops_given_away = 3
    total_lollipops = initial_lollipops + lollipops_from_mom - lollipops_given_away
    result = total_lollipops
    return result

print(solution())