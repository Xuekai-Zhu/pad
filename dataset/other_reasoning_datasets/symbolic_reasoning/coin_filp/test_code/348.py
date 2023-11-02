def solution():
    coin = True
    people = {
        "Braulio": True,
        "Staci": False,
        "Jocelyn": False,
        "Brittany": True
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