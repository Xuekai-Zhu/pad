def solution():
    """James has 3 fish tanks. 1 of the tanks has 20 fish in it and the other two have twice as many fish each as the first. How many total fish do they have?"""
    tank1_fish = 20
    tank2_fish = 2 * tank1_fish
    tank3_fish = 2 * tank1_fish
    total_fish = tank1_fish + tank2_fish + tank3_fish
    result = total_fish
    return result

print(solution())