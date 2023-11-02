def solution():
    coin = True
    people = {
        "Charity": True,
        "Svetlana": False,
        "Jamie": False,
        "Jose A": False
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