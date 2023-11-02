def solution():
    coin = True
    people = {
        "Glenda": True,
        "Beverly": True,
        "Agustin": True,
        "Igor": False
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