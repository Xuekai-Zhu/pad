def solution():
    coin = True
    people = {
        "Krishna": True,
        "Catalina": False,
        "Eileen": False,
        "Teddy": True
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