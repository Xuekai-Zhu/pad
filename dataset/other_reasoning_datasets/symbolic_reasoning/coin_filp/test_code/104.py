def solution():
    coin = True
    people = {
        "Jordan": False,
        "Yoni": True,
        "Lawrence": False,
        "Aura": True
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