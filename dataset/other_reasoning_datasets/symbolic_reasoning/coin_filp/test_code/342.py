def solution():
    coin = True
    people = {
        "Seth": True,
        "Dario": True,
        "Anne": True,
        "Jodie": True
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