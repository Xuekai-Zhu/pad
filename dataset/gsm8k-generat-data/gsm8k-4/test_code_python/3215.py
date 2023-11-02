def solution():
    """A special balloon increases by two-fifths of its previous volume every hour when placed under water. If its original volume is 500cm³, what will its volume be after 2 hours underwater?"""
    # Define the initial volume and growth rate
    initial_volume = 500
    growth_rate = 2/5

    # Calculate the volume after 2 hours
    final_volume = initial_volume * (1 + growth_rate) ** 2

    # Round the volume to the nearest cm³
    result = round(final_volume)

    return result

print(solution())