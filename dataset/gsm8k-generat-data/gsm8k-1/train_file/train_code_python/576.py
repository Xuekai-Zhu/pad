def solution():
    """At a roller derby, 4 teams are competing. Each team is made up of 10 members, and each member needs a pair of roller skates to compete in and another pair of skates as a backup. None of the skates have laces yet, so each member is offered 3 sets of laces per pair of skates. How many sets of laces have been handed out?"""
    num_teams = 4
    team_size = 10
    num_skates = num_teams * team_size * 2
    num_laces_per_skate = 3
    num_laces = num_skates * num_laces_per_skate
    result = num_laces
    return result

print(solution())