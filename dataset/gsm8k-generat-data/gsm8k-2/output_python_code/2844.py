def solution():
    """A mosquito sucks 20 drops of blood every time it feeds on someone. If there are 5000 drops per liter and you have to lose 3 liters of blood to die, how many mosquitoes would have to feed on you to kill you?"""
    drops_per_liter = 5000
    liters_to_die = 3
    drops_to_die = drops_per_liter * liters_to_die
    drops_per_bite = 20
    mosquitos_to_die = drops_to_die / drops_per_bite
    result = mosquitos_to_die
    return result

print(solution())