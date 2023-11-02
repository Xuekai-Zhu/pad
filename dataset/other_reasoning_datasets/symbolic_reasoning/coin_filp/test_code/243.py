def solution():
    coin = True
    people = {
        "Lalo": False,
        "Yolanda": True,
        "Elida": False,
        "Ester": True
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