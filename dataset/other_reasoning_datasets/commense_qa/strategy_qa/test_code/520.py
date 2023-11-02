def solution():
    salmon_reproduce_in_freshwater = True
    caspian_sea_is_saltwater = True
    if salmon_reproduce_in_freshwater and not caspian_sea_is_saltwater:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())