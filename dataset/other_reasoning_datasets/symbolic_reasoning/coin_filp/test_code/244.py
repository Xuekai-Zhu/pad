def solution():
    coin = True
    people = {
        "Miriam": False,
        "Brandy": True,
        "Bertha": True,
        "Renato": True
    }
    for person, flips in people.items():
        if flips:
            coin = not coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())