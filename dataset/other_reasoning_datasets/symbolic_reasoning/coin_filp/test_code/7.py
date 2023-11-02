def solution():
    coin = True
    people = {
        "Beatriz": True,
        "Gillian": False,
        "Coco": False,
        "Vivian": False
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