def solution():
    """The Franzia wine is three times as old as the Carlo Rosi, while the Carlo Rosi is four times older than the Twin Valley. Calculate the total age of the three brands of wine if the Carlo Rosi is 40 years old."""
    # Define the age of Carlo Rosi
    carlo_rosi = 40

    # Calculate the age of Twin Valley
    twin_valley = carlo_rosi / 4

    # Calculate the age of Franzia
    franzia = carlo_rosi * 3

    # Calculate the total age of the three brands of wine
    total_age = carlo_rosi + twin_valley + franzia

    # return the result
    result = total_age
    return result

print(solution())