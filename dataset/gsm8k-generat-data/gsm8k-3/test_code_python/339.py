def solution():
    """At a gathering, it was reported that 26 people took wine, 22 people took soda, and 17 people took both drinks. If each person could have taken one or more drinks regardless of what was reported, how many people altogether were at the gathering?"""
    # Use the inclusion-exclusion principle to calculate the total number of people
    total_people = 26 + 22 - 17

    # Display the total number of people
    result = total_people
    return result

print(solution())