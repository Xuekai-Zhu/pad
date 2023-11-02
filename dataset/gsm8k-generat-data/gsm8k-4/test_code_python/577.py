def solution():
    """At a roller derby, 4 teams are competing. Each team is made up of 10 members, and each member needs a pair of roller skates to compete in and another pair of skates as a backup. None of the skates have laces yet, so each member is offered 3 sets of laces per pair of skates. How many sets of laces have been handed out?"""
    # Define the number of teams and members per team
    num_teams = 4
    members_per_team = 10

    # Calculate the total number of pairs of skates needed
    pairs_of_skates = num_teams * members_per_team * 2

    # Calculate the total number of sets of laces needed
    sets_of_laces = pairs_of_skates * 3

    # Return the result
    result = sets_of_laces
    return result

print(solution())