def solution():
    coin = True
    people = {
        "Dusty": False,
        "Yanet": True,
        "Hortencia": True,
        "Lili": True
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