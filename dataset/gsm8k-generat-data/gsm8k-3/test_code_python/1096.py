def solution():
    """Rory has 30 more jellybeans than her sister Gigi who has 15 jellybeans.  Lorelai has already eaten three times the number of jellybeans that both girls have.  How many jellybeans has Lorelai eaten?"""
    # Define the number of jellybeans each girl has
    gigi_jellybeans = 15
    rory_jellybeans = gigi_jellybeans + 30

    # Calculate the total number of jellybeans both girls have
    total_jellybeans = gigi_jellybeans + rory_jellybeans

    # Calculate the number of jellybeans Lorelai has eaten
    lorelai_jellybeans = 3 * total_jellybeans

    # Display the number of jellybeans Lorelai has eaten
    result = lorelai_jellybeans
    return result

print(solution())