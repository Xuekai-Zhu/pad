def solution():
    """It was Trevor's job to collect fresh eggs from the family's 4 chickens every morning. He got 4 eggs from Gertrude and 3 eggs from Blanche. Nancy laid 2 eggs as did Martha. On the way, he dropped 2 eggs. How many eggs did Trevor have left?"""
    # Define the number of eggs collected from each chicken
    gertrude_eggs = 4
    blanche_eggs = 3
    nancy_eggs = 2
    martha_eggs = 2

    # Calculate the total number of eggs collected
    total_eggs = gertrude_eggs + blanche_eggs + nancy_eggs + martha_eggs

    # Subtract the number of eggs dropped
    total_eggs -= 2

    # return the result
    result = total_eggs
    return result

print(solution())