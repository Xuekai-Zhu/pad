def solution():
    napkins_given_by_olivia = 10
    napkins_given_by_amelia = 2 * napkins_given_by_olivia
    napkins_before = 15
    napkins_after = napkins_before + napkins_given_by_olivia + napkins_given_by_amelia
    result = napkins_after
    return result

print(solution())