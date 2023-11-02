def solution():
    number_of_teams = 4  # There are 4 teams competing
    members_per_team = 10  # Each team is made up of 10 members
    pairs_of_skates_per_member = 2  # Each member needs a pair of skates to compete in and another pair as a backup
    sets_of_laces_per_skate = 3  # Each pair of skates is offered 3 sets of laces

    # Calculate the total number of pairs of skates
    total_pairs_of_skates = number_of_teams * members_per_team * pairs_of_skates_per_member

    # Calculate the total number of sets of laces
    total_sets_of_laces = total_pairs_of_skates * sets_of_laces_per_skate
    result = total_sets_of_laces
    return result

print(solution())