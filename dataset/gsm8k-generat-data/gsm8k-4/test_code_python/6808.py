def solution():
    """To get his fill of oysters, Crabby has to eat at least twice as many oysters as Squido does. If Squido eats 200 oysters, how many oysters do they eat altogether?"""
    # Define the number of oysters Squido eats
    squido_oysters = 200

    # Define the minimum number of oysters Crabby eats
    crabby_oysters = squido_oysters * 2

    # Calculate the total number of oysters eaten
    total_oysters = squido_oysters + crabby_oysters

    # Return the result
    result = total_oysters
    return result

print(solution())