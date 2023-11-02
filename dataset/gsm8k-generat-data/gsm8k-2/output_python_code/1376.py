def solution():
    """A teacher asked Adelaide, Ephraim, and Kolton to buy ducks and monitor their growth patterns and features for their science class. Adelaide bought twice the number of ducks that Ephraim bought, while Ephraim bought 45 fewer ducks than Kolton. If Adelaide bought 30 ducks, what's the average number of ducks the three bought?"""
    adelaide_ducks = 30
    ephraim_ducks = adelaide_ducks / 2
    kolton_ducks = ephraim_ducks + 45
    total_ducks = adelaide_ducks + ephraim_ducks + kolton_ducks
    average_ducks = total_ducks / 3
    result = average_ducks
    return result

print(solution())