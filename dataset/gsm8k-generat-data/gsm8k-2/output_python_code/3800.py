def solution():
    """Safari National park has 100 lions, half as many snakes, and 10 fewer giraffes than snakes. On the other hand, Savanna National park has double as many lions as Safari National park, triple as many snakes as Safari National park, and 20 more giraffes than Safari National park. How many animals in total does Savanna National park have?"""
    safari_lions = 100
    safari_snakes = safari_lions / 2
    safari_giraffes = safari_snakes - 10
    savanna_lions = 2 * safari_lions
    savanna_snakes = 3 * safari_snakes
    savanna_giraffes = safari_giraffes + 20
    total_animals = savanna_lions + savanna_snakes + savanna_giraffes
    result = total_animals
    return result

print(solution())