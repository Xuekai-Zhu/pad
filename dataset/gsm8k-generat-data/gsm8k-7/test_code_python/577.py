def solution():
    num_teams = 4
    num_members = 10
    num_skates_per_member = 2
    num_laces_per_skate = 3

    # Calculate the total number of skates needed
    total_skates = num_teams * num_members * num_skates_per_member

    # Calculate the total number of lace sets needed
    total_laces = total_skates * num_laces_per_skate
    result = total_laces
    return result

print(solution())