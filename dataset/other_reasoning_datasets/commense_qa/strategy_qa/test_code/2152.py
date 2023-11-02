def solution():
    felony_jury_size = 12
    bunco_min_players = 12
    if felony_jury_size >= bunco_min_players:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())