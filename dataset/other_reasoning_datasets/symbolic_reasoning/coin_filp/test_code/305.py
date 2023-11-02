def solution():
    coin = True
    people = {
        "Todd": True,
        "Joni": True,
        "Gil": True,
        "Fran": False
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