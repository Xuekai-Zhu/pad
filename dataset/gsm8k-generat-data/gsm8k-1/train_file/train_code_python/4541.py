def solution():
    """James has 3 fish tanks. 1 of the tanks has 20 fish in it and the other two have twice as many fish each as the first. How many total fish do they have?"""
    first_tank_fish = 20
    second_tank_fish = first_tank_fish * 2
    third_tank_fish = first_tank_fish * 2
    total_fish = first_tank_fish + second_tank_fish + third_tank_fish
    result = total_fish
    return result

print(solution())