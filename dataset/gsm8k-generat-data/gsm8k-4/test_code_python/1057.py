def solution():
    """Twenty gallons of tea were poured into 80 containers. Geraldo drank 3.5 containers. How many pints of tea did Geraldo drink?"""
    # Define the volume of tea in gallons and the total number of containers
    tea_gallons = 20
    total_containers = 80

    # Calculate the volume of tea in each container
    tea_per_container = tea_gallons / total_containers

    # Calculate the number of pints of tea that Geraldo drank
    gerardo_drunk = 3.5 * tea_per_container * 8

    result = gerardo_drunk
    return result

print(solution())