def solution():
    coin = True
    people = {
        "Camilo": True,
        "Becky": False,
        "Eliza": False,
        "Rebecca": False
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