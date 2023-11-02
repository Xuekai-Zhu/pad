def solution():
    """At a gathering, it was reported that 26 people took wine, 22 people took soda, and 17 people took both drinks. If each person could have taken one or more drinks regardless of what was reported, how many people altogether were at the gathering?"""
    wine_takers = 26
    soda_takers = 22
    both_takers = 17
    total_takers = wine_takers + soda_takers - both_takers
    result = total_takers
    return result

print(solution())