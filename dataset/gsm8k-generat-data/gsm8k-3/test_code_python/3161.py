def solution():
    """It was Trevor's job to collect fresh eggs from the family's 4 chickens every morning.   He got 4 eggs from Gertrude and 3 eggs from Blanche.  Nancy laid 2 eggs as did Martha.  On the way, he dropped 2 eggs.  How many eggs did Trevor have left?"""
    # Calculate the total number of eggs collected
    total_eggs = 4 + 3 + 2 + 2

    # Subtract the number of eggs that were dropped
    remaining_eggs = total_eggs - 2

    # Display the number of eggs Trevor has left
    result = remaining_eggs
    return result

print(solution())