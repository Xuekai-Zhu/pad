def solution():
    coin = True
    people = {
        "Salma": False,
        "Pj": True,
        "Gladis": True,
        "Monica": True
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