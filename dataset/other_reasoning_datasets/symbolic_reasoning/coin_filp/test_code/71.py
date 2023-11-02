def solution():
    coin = True
    people = {
        "Sally": True,
        "Sadie": True,
        "Christie": False,
        "Ellie": True
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