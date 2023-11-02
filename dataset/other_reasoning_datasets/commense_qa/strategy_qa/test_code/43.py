def solution():
    lefty_grove_nicknames = ["Lefty Grove"]
    pablo_escobar_nicknames = ["Don Pablo", "El Padrino", "El Patrón"]
    if len(pablo_escobar_nicknames) > len(lefty_grove_nicknames):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())