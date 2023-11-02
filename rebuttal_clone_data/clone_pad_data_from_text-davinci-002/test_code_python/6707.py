def solution():
    original_sheep = 400
    sheep_given_away = original_sheep / 4 + original_sheep / 2
    sheep_remaining = original_sheep - sheep_given_away
    result = sheep_remaining
    return result

print(solution())