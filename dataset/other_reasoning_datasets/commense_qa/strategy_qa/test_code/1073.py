def solution():
    napoleonic_wars_start = 1803
    napoleonic_wars_end = 1815
    first_nuclear_bomb_used = 1945
    if first_nuclear_bomb_used < napoleonic_wars_start or first_nuclear_bomb_used > napoleonic_wars_end:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())