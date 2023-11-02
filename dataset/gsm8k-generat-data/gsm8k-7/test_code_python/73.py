def solution():
    num_players = 13
    num_coaches = 3
    num_helpers = 2
    total_people = num_players + num_coaches + num_helpers
    num_packs = ((total_people - 1) // 6) + 1
    result = num_packs
    return result

print(solution())