def solution():
    coin = True
    people = {
        "Hilario": True,
        "Magdalena": True,
        "Morris": True,
        "Patricio": False
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