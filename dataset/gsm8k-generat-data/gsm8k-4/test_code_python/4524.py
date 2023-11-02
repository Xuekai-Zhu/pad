def solution():
    """Johann had 60 oranges. He decided to eat 10. Once he ate them, half were stolen by Carson. Carson returned exactly 5. How many oranges does Johann have now?"""
    # Define the initial number of oranges
    oranges_initial = 60

    # Johann eats 10 oranges
    oranges_johann = oranges_initial - 10

    # Half of the remaining oranges are stolen by Carson
    oranges_carson = oranges_johann / 2

    # Carson returns 5 oranges
    oranges_carson += 5

    # Calculate the total number of oranges Johann has now
    oranges_final = oranges_johann - oranges_carson

    # Return the result
    result = oranges_final
    return result

print(solution())