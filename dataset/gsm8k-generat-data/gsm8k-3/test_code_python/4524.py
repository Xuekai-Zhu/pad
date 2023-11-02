def solution():
    """Johann had 60 oranges. He decided to eat 10. Once he ate them, half were stolen by Carson. Carson returned exactly 5. How many oranges does Johann have now?"""
    # Define the initial number of oranges Johann had
    initial_oranges = 60

    # Calculate the number of oranges Johann has after eating 10
    oranges_after_eating = initial_oranges - 10

    # Calculate the number of oranges stolen by Carson
    oranges_stolen = oranges_after_eating / 2

    # Calculate the number of oranges Johann has after Carson returned 5
    oranges_after_carson = oranges_stolen + 5

    # Display the number of oranges Johann has now
    result = oranges_after_carson
    return result

print(solution())