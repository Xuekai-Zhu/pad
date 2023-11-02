def solution():
    container_size = 45  # in pounds
    container_price = 21  # in dollars
    litter_box_size = 15  # in pounds
    change_frequency = 7  # in days
    total_days = 210

    # Calculate the total amount of litter needed for 210 days
    total_litter_needed = (litter_box_size * 1.0 / container_size) * (total_days / change_frequency)

    # Calculate the total number of containers needed
    total_containers_needed = total_litter_needed / litter_box_size

    # Calculate the total cost of all containers needed
    total_cost = total_containers_needed * container_price
    result = total_cost
    return result

print(solution())