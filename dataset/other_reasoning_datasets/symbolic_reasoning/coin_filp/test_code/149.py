def solution():
    coin = True
    people = {
        "Donnie": False,
        "Alli": False,
        "Terry": True,
        "Krystal": False
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