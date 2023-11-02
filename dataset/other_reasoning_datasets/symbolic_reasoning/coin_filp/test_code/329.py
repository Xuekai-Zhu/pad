def solution():
    coin = True
    people = {
        "Wesley": False,
        "Marcelo": False,
        "Rodolfo": True,
        "Erick": False
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