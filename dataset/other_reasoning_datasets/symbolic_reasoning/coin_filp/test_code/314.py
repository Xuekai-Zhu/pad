def solution():
    coin = True
    people = {
        "Yazmin": True,
        "Lea": False,
        "Rodrigo": False,
        "Sammy": True
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