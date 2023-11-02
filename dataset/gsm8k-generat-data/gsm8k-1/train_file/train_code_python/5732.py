def solution():
    """The total number of years in a century is the same as the number of marbles Gideon has. If he gives 3/4 of the marbles to his sister and multiples the number of remaining marbles by 2, he gets his age five years from now. How old is Gideon now?"""
    years_in_century = 100
    marbles = years_in_century
    marbles_given_to_sister = marbles * 3/4
    remaining_marbles = marbles - marbles_given_to_sister
    age_in_five_years = remaining_marbles * 2
    current_age = age_in_five_years - 5
    result = current_age
    return result

print(solution())