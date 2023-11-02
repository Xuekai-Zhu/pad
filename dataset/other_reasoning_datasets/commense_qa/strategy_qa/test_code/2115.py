def solution():
    christina_aguilera = True
    kelly_clarkson = True
    judges_only_turn_for_competitors = True
    kelly_has_not_competed = True
    if christina_aguilera and kelly_clarkson and judges_only_turn_for_competitors and kelly_has_not_competed:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())