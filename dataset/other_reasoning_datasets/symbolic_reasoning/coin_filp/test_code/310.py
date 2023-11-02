def solution():
    coin = True
    people = {
        "Maritza": False,
        "Nana": False,
        "Loretta": True,
        "Eric": False
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