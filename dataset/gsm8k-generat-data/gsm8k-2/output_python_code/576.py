def solution():
    """At a roller derby, 4 teams are competing. Each team is made up of 10 members, and each member needs a pair of roller skates to compete in and another pair of skates as a backup. None of the skates have laces yet, so each member is offered 3 sets of laces per pair of skates. How many sets of laces have been handed out?"""
    teams = 4
    members_per_team = 10
    pairs_per_member = 2
    laces_per_pair = 3
    total_laces = teams * members_per_team * pairs_per_member * laces_per_pair
    result = total_laces
    return result

print(solution())