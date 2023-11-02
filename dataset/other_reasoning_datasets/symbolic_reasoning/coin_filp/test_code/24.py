def solution():
    coin = True
    people = {
        "Mauricio": True,
        "Lee": False,
        "Madi": False,
        "Lizzie": True
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