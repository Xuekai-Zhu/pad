def solution():
    japanese_street_aesthetic = "neon"
    noble_gasses = ["neon", "argon", "helium", "krypton", "xenon", "radon"]
    if japanese_street_aesthetic in noble_gasses:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())