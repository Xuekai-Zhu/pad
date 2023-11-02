def solution():
    """Gertrude the chicken has 10 fleas. The other chicken, Maud has 5 times the amount of fleas as Olive. The final chicken, Olive has half the amount of flees as Gertrude. How many fleas are there?"""
    gertrude_fleas = 10
    olive_fleas = gertrude_fleas / 2
    maud_fleas = 5 * olive_fleas
    total_fleas = gertrude_fleas + olive_fleas + maud_fleas
    result = total_fleas
    return result

print(solution())