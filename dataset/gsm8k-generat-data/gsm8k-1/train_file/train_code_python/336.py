def solution():
    """At a gathering, it was reported that 26 people took wine, 22 people took soda, and 17 people took both drinks. If each person could have taken one or more drinks regardless of what was reported, how many people altogether were at the gathering?"""
    wine_drinkers = 26
    soda_drinkers = 22
    both_drinkers = 17
    total_drinkers = wine_drinkers + soda_drinkers - both_drinkers
    result = total_drinkers
    return result

print(solution())