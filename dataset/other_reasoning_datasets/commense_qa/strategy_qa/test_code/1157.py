def solution():
    alligator_has_saltwater_glands = False
    crocodile_has_saltwater_glands = True
    if alligator_has_saltwater_glands or not crocodile_has_saltwater_glands:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())