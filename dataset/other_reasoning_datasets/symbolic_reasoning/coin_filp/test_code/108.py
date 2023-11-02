def solution():
    coin = True
    people = {
        "Raymundo": True,
        "Jonathon": True,
        "Lexi": False,
        "Rony": True
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