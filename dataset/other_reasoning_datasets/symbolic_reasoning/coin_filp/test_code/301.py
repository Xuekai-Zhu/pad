def solution():
    coin = True
    people = {
        "Caroline": True,
        "Demetrius": True,
        "Fidel": False,
        "Solomon": True
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