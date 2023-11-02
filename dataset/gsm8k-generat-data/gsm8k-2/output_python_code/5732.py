def solution():
    """The total number of years in a century is the same as the number of marbles Gideon has. If he gives 3/4 of the marbles to his sister and multiples the number of remaining marbles by 2, he gets his age five years from now. How old is Gideon now?"""
    marbles = 100
    gideon_age_in_5_years = (marbles * (1 - 3/4)) * 2
    gideon_current_age = gideon_age_in_5_years - 5
    result = gideon_current_age
    return result

print(solution())