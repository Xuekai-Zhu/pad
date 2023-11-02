def solution():
    """To get to work, Ryan bikes one day a week takes the bus three times a week and gets a ride from a friend once a week. It takes him thirty minutes to bike to work. The bus takes ten minutes longer since it stops at every bus stop for other passengers. His friend driving him is the fastest and cuts two-thirds off his biking time. How many minutes does he spend every week commuting to work?"""
    # Define the time it takes Ryan to bike to work
    bike_time = 30 # in minutes

    # Define the additional time it takes for the bus
    bus_additional_time = 10 # in minutes

    # Define the time saved by riding with his friend
    saved_time = (2/3) * bike_time # in minutes

    # Calculate the total time Ryan spends commuting to work each week
    total_time = (bike_time + bus_additional_time) * 3 + saved_time + bike_time

    # Display the total time
    result = total_time
    return result

print(solution())