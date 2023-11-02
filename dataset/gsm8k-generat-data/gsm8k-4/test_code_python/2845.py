def solution():
    """A mosquito sucks 20 drops of blood every time it feeds on someone. If there are 5000 drops per liter and you have to lose 3 liters of blood to die, how many mosquitoes would have to feed on you to kill you?"""
    # Define the number of drops per liter and the amount of blood required to die
    DROPS_PER_LITER = 5000
    BLOOD_TO_DIE = 3

    # Calculate the total number of drops in the required blood volume
    total_drops = DROPS_PER_LITER * BLOOD_TO_DIE

    # Calculate the number of mosquito feeds required to reach the fatal blood volume
    feeds_to_die = total_drops / 20

    # Round up to the nearest integer
    result = int(feeds_to_die + 0.5)

    return result

print(solution())