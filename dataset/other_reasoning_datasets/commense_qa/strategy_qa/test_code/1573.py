def solution():
    # Define the historical events and the law
    burr_kills_hamilton = True
    burr_continues_vp = True
    stand_your_ground = True
    # Check if the Vice President can kill with impunity
    if burr_kills_hamilton and burr_continues_vp and stand_your_ground:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())