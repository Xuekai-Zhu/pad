def solution():
    """The Franzia wine is three times as old as the Carlo Rosi, while the Carlo Rosi is four times older than the Twin Valley. Calculate the total age of the three brands of wine if the Carlo Rosi is 40 years old."""
    # Calculate the age of the Twin Valley
    twin_valley_age = 40 / 4

    # Calculate the age of the Carlo Rosi and Franzia
    carlo_rosi_age = 40
    franzia_age = 3 * carlo_rosi_age

    # Calculate the total age of the three brands of wine
    total_age = twin_valley_age + carlo_rosi_age + franzia_age

    # Display the total age
    result = total_age
    return result

print(solution())