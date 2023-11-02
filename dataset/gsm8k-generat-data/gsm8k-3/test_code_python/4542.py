def solution():
    """James has 3 fish tanks.  1 of the tanks has 20 fish in it and the other two have twice as many fish each as the first. How many total fish do they have?"""
    # Define the number of fish in the first tank
    tank1_fish = 20

    # Calculate the number of fish in the second and third tanks
    tank2_fish = tank1_fish * 2
    tank3_fish = tank1_fish * 2

    # Calculate the total number of fish
    total_fish = tank1_fish + tank2_fish + tank3_fish

    # Display the total number of fish
    result = total_fish
    return result

print(solution())