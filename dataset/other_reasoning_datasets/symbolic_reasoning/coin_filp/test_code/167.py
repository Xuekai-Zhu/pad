def solution():
    coin = True
    people = {
        "Lacey": True,
        "Nora": False,
        "Debra": False,
        "Ashleigh": False
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