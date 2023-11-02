def solution():
    num_guests = 20
    hot_dogs_per_guest = 2
    num_left_over = 4
    num_hot_dogs_per_pack = 6
    cost_per_pack = 2.0

    # Calculate the total number of hot dogs needed
    total_hot_dogs = num_guests * hot_dogs_per_guest

    # Calculate the total number of hot dogs needed
    total_hot_dogs_needed = total_hot_dogs - num_left_over + num_hot_dogs_needed

    # Calculate the total cost of all hot dogs needed
    total_cost = total_hot_dogs_needed * cost_per_pack
    result = total_cost
    return result

print(solution())