def solution():
    shinto_has_restrictions = False
    kosher_laws_prohibit_shellfish = True
    if shinto_has_restrictions or not kosher_laws_prohibit_shellfish:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())