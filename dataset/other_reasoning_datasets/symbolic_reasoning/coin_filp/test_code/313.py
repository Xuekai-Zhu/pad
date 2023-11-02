def solution():
    coin = True
    people = {
        "Jenni": True,
        "Leonel": True,
        "Micheal": False,
        "Kat": False
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