def solution():
    """A teacher asked Adelaide, Ephraim, and Kolton to buy ducks and monitor their growth patterns and features for their science class. Adelaide bought twice the number of ducks that Ephraim bought, while Ephraim bought 45 fewer ducks than Kolton. If Adelaide bought 30 ducks, what's the average number of ducks the three bought?"""
    # Adelaide bought twice the number of ducks that Ephraim bought
    ephraim_ducks = (30 / 2)

    # Ephraim bought 45 fewer ducks than Kolton
    kolton_ducks = ephraim_ducks + 45

    # Calculate the total number of ducks
    total_ducks = 30 + ephraim_ducks + kolton_ducks

    # Calculate the average number of ducks
    average_ducks = total_ducks / 3

    # Display the average number of ducks
    result = average_ducks
    return result

print(solution())