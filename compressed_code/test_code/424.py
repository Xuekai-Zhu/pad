def solution():
    
    teams = 4
    members_per_team = 10
    pairs_per_member = 2
    laces_per_pair = 3
    total_laces = teams * members_per_team * pairs_per_member * laces_per_pair
    result = total_laces
    return result

print(solution())