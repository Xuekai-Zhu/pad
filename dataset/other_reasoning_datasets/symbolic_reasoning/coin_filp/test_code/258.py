def solution():
    coin = True
    people = {
        "Daryl": False,
        "Owen": False,
        "Myra": True,
        "Aaron": False
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