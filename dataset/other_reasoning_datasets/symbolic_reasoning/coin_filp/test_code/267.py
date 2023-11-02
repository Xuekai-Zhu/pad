def solution():
    coin = True
    people = {
        "Andy": False,
        "Cecilia": True,
        "Gretchen": True,
        "Sandi": True
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