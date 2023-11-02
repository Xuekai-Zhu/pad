def solution():
    coin = True
    people = {
        "Georgina": True,
        "Joshua": True,
        "Lindsey": False,
        "César": True
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