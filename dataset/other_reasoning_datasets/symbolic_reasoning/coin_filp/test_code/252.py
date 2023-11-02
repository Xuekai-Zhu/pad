def solution():
    coin = True
    people = {
        "Jodi": True,
        "Judi": True,
        "Nia": False,
        "Raj": True
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