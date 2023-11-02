def solution():
    # Calculate the total number of fish already housed in the 3 tanks
    total_fish_in_first_tanks = 3 * 15

    # Calculate the number of fish that Jennifer still needs to house
    remaining_fish = 75 - total_fish_in_first_tanks

    # Calculate how many more tanks Jennifer needs to build to house the remaining fish
    additional_tanks_needed = remaining_fish // 10

    result = additional_tanks_needed
    return result

print(solution())