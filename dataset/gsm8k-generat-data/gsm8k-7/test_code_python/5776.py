def solution():
    reapplication_time = 2  # hours
    sunscreen_per_application = 3  # ounces
    sunscreen_bottle_size = 12  # ounces
    sunscreen_bottle_cost = 3.5

    # Calculate the number of times Tiffany will need to reapply sunscreen
    num_reapplications = 16 // reapplication_time

    # Calculate the total amount of sunscreen needed for the entire trip
    total_sunscreen_needed = num_reapplications * sunscreen_per_application

    # Calculate the number of sunscreen bottles needed
    num_bottles_needed = total_sunscreen_needed / sunscreen_bottle_size

    # Calculate the total cost of all sunscreen bottles needed
    total_cost = num_bottles_needed * sunscreen_bottle_cost
    result = total_cost
    return result

print(solution())