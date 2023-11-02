def solution():
    # Calculate the number of ducks at North Pond based on the number at Lake Michigan
    ducks_at_Lake_Michigan = 100
    ducks_at_North_Pond = 6 + 2*ducks_at_Lake_Michigan
    result = ducks_at_North_Pond
    return result

print(solution())