def solution():
    coin = True
    people = {
        "Cristobal": True,
        "Dania": False,
        "Li": False,
        "Anna": True
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