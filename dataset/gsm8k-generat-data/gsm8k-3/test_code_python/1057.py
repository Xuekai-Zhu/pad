def solution():
    """Twenty gallons of tea were poured into 80 containers. Geraldo drank 3.5 containers. How many pints of tea did Geraldo drink?"""
    # Define the conversion factor from gallons to pints
    GALLONS_TO_PINTS = 8

    # Define the number of gallons of tea poured and the number of containers
    gallons = 20
    containers = 80

    # Calculate the total number of pints of tea in all the containers
    total_pints = gallons * GALLONS_TO_PINTS * containers

    # Calculate the number of pints of tea Geraldo drank
    gerardo_containers = 3.5
    gerardo_pints = gerardo_containers * GALLONS_TO_PINTS

    # Display the number of pints of tea Geraldo drank
    result = gerardo_pints
    return result

print(solution())