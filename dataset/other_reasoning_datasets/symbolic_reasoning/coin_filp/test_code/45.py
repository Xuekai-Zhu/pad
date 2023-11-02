def solution():
    coin = True
    people = {
        "Ashish": True,
        "Tracey": True,
        "Varun": False,
        "Emil": True
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