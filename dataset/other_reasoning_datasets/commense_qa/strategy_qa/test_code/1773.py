def solution():
    hanging_requires_rope = True
    ships_have_rope = True
    if hanging_requires_rope and ships_have_rope:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())