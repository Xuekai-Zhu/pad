def solution():
    """Safari National park has 100 lions, half as many snakes, and 10 fewer giraffes than snakes. On the other hand, Savanna National park has double as many lions as Safari National park, triple as many snakes as Safari National park, and 20 more giraffes than Safari National park. How many animals in total does Savanna National park have?"""
    # Calculate the number of snakes in Safari National park
    snakes_safari = 100 / 2

    # Calculate the number of giraffes in Safari National park
    giraffes_safari = snakes_safari - 10

    # Calculate the number of lions, snakes, and giraffes in Savanna National park
    lions_savanna = 2 * 100
    snakes_savanna = 3 * 100
    giraffes_savanna = giraffes_safari + 20

    # Calculate the total number of animals in Savanna National park
    total_animals_savanna = lions_savanna + snakes_savanna + giraffes_savanna

    # return the result
    result = total_animals_savanna
    return result

print(solution())