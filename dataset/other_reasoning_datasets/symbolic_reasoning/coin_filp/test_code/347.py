def solution():
    coin = True
    people = {
        "Rohan": True,
        "Antoinette": False,
        "Nikki": True,
        "Aida": False
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