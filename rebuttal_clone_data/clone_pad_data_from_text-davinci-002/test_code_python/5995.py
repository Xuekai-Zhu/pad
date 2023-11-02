def solution():
    sheep_mary_has = 300
    sheep_bob_has = (2 * sheep_mary_has) + 35
    sheep_mary_needs = sheep_bob_has - 69 - sheep_mary_has
    result = sheep_mary_needs
    return result

print(solution())