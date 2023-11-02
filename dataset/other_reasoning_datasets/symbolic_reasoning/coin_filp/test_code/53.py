def solution():
    coin = True
    people = {
        "Micaela": False,
        "Kevin": True,
        "Diamond": False,
        "Ty": False
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