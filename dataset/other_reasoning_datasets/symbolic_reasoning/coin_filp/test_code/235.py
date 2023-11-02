def solution():
    coin = True
    people = {
        "Claudia": True,
        "Cole": False,
        "Matthew": False,
        "Juan Pablo": False
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