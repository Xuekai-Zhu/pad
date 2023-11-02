def solution():
    first_half_starters = 11
    first_half_subs = 2
    second_half_subs = first_half_subs * 2
    total_subs = first_half_subs + second_half_subs
    total_players = 24
    result = total_players - (first_half_starters + total_subs)
    return result

print(solution())