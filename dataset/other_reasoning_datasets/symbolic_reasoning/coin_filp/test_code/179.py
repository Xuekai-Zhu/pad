def solution():
    coin = True
    people = {
        "Efrain": False,
        "Rickey": False,
        "Jonathan": True,
        "Kelli": False
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