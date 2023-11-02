def solution():
    """Ali, Peter, and Joey were fishing. The fish Ali caught weighed, in sum, twice as much as the fish that Peter caught. Joey caught 1 kg more fish than Peter. Together the three of them caught 25 kg of fish. How many kilograms did Ali catch?"""
    total_fish_weight = 25
    peter_fish_weight = x
    joey_fish_weight = peter_fish_weight + 1
    ali_fish_weight = 2 * peter_fish_weight

    # Set up equation system
    total_fish_weight = peter_fish_weight + joey_fish_weight + ali_fish_weight
    total_fish_weight = 25
    eq1 = peter_fish_weight + joey_fish_weight + ali_fish_weight - total_fish_weight
    eq2 = ali_fish_weight - 2 * peter_fish_weight
    eq3 = joey_fish_weight - peter_fish_weight - 1

    # Solve system of equations
    solution = sympy.solve((eq1, eq2, eq3), (peter_fish_weight, ali_fish_weight, joey_fish_weight))
    result = solution[1]
    return result

print(solution())