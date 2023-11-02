def solution():
    num_guests = 120
    num_glasses_per_guest = 2
    num_servings_per_bottle = 6

    # Calculate the total number of servings of champagne needed
    total_servings = num_guests * num_glasses_per_guest

    # Calculate the total number of bottles of champagne needed
    total_bottles = total_servings / num_servings_per_bottle

    result = total_bottles
    return result

print(solution())