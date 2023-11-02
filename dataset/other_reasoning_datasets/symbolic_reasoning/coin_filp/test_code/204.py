def solution():
    coin = True
    people = {
        "Sandeep": True,
        "Graciela": False,
        "Jai": True,
        "Xiomara": False
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