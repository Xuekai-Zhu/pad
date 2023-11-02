def solution():
    is_martyr_saint = True
    was_excommunicated = True
    if is_martyr_saint and not was_excommunicated:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())