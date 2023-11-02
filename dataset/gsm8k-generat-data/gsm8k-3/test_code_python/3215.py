def solution():
    """A special balloon increases by two-fifths of its previous volume every hour when placed under water. If its original volume is 500cm³, what will its volume be after 2 hours underwater?"""
    
    # Define the original volume and time underwater
    original_volume = 500
    time_underwater = 2

    # Calculate the volume of the balloon after 2 hours
    volume = original_volume * ((2/5) ** time_underwater)

    # Display the updated volume
    result = volume
    return result

print(solution())