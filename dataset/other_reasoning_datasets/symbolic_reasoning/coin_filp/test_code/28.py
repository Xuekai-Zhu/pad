def solution():
    coin = True
    people = {
        "Margarita": True,
        "Anabel": True,
        "Shaun": True,
        "Celina": True
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