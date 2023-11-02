def solution():
    coin = True
    people = {
        "Michele": True,
        "Karan": False,
        "Abraham": False,
        "Ellen": True
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