def solution():
    """Alex, Stan, and Adelwolfe are trying to catch them all, Pokemon that is. Together they have caught 339 Pokemon. Alex has caught 5 more than Stan, and Stan has caught 13 less than 4 times as many as Adelwolfe has caught. How many Pokemon has Stan caught?"""
    total_pokemon = 339
    adelwolfe_pokemon = (total_pokemon - 5) / 17
    stan_pokemon = 4 * adelwolfe_pokemon - 13
    result = stan_pokemon
    return result

print(solution())