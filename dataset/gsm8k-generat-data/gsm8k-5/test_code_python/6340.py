def solution():
    milk_per_shake = 4  # Blake needs 4 ounces of milk per milkshake
    ice_cream_per_shake = 12  # Blake needs 12 ounces of ice cream per milkshake
    milk_available = 72  # Blake has 72 ounces of milk
    ice_cream_available = 192  # Blake has 192 ounces of ice cream

    # Calculate the maximum number of milkshakes Blake can make with the available ingredients
    max_shakes_with_milk = milk_available / milk_per_shake
    max_shakes_with_ice_cream = ice_cream_available / ice_cream_per_shake
    max_shakes = min(max_shakes_with_milk, max_shakes_with_ice_cream)

    # Calculate the total amount of milk used
    total_milk_used = max_shakes * milk_per_shake

    # Calculate the amount of milk left over
    milk_left_over = milk_available - total_milk_used
    result = milk_left_over
    return result

print(solution())