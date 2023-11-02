def solution():
    coin = True
    people = {
        "Janice": True,
        "Shelly": True,
        "Arnulfo": False,
        "Nestor": True
    }
    for person, flips in people.items():
        if flips:
            # Flip the coin by reversing its current state
            coin = not coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())