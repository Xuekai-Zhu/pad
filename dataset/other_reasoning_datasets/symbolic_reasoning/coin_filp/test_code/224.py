def solution():
    coin = True
    people = {
        "Alfonso": False,
        "Collin": False,
        "Amado": False,
        "Dick": True
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