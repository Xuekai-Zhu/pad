def solution():
    coin = True
    people = {
        "Irvin": False,
        "Brittney": True,
        "Vince": True,
        "Lucas": False
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