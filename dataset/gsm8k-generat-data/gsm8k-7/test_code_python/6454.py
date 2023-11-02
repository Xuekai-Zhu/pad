def solution():
    original_group = 9
    new_group = 2 + 3 * original_group
    half_new_group = new_group / 2
    remaining_turtles = original_group + half_new_group
    result = remaining_turtles
    return result

print(solution())