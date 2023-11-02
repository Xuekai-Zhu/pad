def solution():
    """A mosquito sucks 20 drops of blood every time it feeds on someone. If there are 5000 drops per liter and you have to lose 3 liters of blood to die, how many mosquitoes would have to feed on you to kill you?"""
    # Define the number of drops per liter of blood
    DROPS_PER_LITER = 5000

    # Calculate the total number of drops of blood in 3 liters
    total_drops = 3 * DROPS_PER_LITER

    # Calculate the number of mosquitoes needed to reach the total number of drops required to die
    mosquitoes_needed = total_drops / 20

    # Display the number of mosquitoes needed to kill
    result = int(mosquitoes_needed)
    return result

print(solution())