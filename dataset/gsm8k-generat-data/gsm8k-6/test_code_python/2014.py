def solution():
    # Calculate the number of fish in the first 3 tanks
    fish_in_first_tanks = 3 * 15

    # Calculate the number of fish that need to be housed in the remaining tanks
    remaining_fish = 75 - fish_in_first_tanks

    # Calculate the number of tanks needed to house the remaining fish
    tanks_needed = remaining_fish / 10

    # Round up the number of tanks to a whole number
    tanks_needed = math.ceil(tanks_needed)

    result = tanks_needed
    return result

print(solution())