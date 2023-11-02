def solution():
    coin = True
    people = {
        "Prince": True,
        "Rene": True,
        "Vishal": True,
        "Patrick": False
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