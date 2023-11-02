def solution():
    tanks_built = 3  # Jennifer has already built 3 tanks
    fish_per_tank_1 = 15  # The first 3 tanks hold 15 fish each
    fish_per_tank_2 = 10  # The remaining tanks will hold 10 fish each
    total_fish = 75  # Jennifer needs to house a total of 75 fish

    # Calculate the total number of fish in the first 3 tanks
    total_fish_tanks_1 = tanks_built * fish_per_tank_1

    # Calculate the number of tanks Jennifer still needs to build
    remaining_fish = total_fish - total_fish_tanks_1
    remaining_tanks = remaining_fish / fish_per_tank_2
    result = remaining_tanks
    return result

print(solution())