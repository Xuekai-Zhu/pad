def solution():
    pangolins_are_nocturnal = True
    clouded_leopards_are_nocturnal = True
    if pangolins_are_nocturnal and clouded_leopards_are_nocturnal:
        result = "possible"
    else:
        result = "unlikely"
    return result

print(solution())