def solution():
    # Define the number of fish in the first tank
    first_tank_fish = 20

    # Define the number of fish in the other two tanks (twice as many as the first tank)
    second_tank_fish = first_tank_fish * 2
    third_tank_fish = first_tank_fish * 2

    # Calculate the total number of fish
    total_fish = first_tank_fish + second_tank_fish + third_tank_fish
    result = total_fish
    return result

print(solution())