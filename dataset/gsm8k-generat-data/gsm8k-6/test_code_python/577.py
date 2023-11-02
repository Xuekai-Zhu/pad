def solution():
    # Calculate the total number of sets of laces handed out
    num_teams = 4
    num_members = 10
    num_skates_per_member = 2
    num_laces_per_skate = 3
    total_laces = num_teams * num_members * num_skates_per_member * num_laces_per_skate
    result = total_laces
    return result

print(solution())