def solution():
    first_hour_rate = 8
    second_hour_rate = 10
    third_hour_rate = 10
    fourth_hour_rate = 14
    leak_rate = 8

    total_time = 5

    # Calculate the total amount of water filled in the first hour
    water_filled_in_first_hour = first_hour_rate * 1

    # Calculate the total amount of water filled in the next two hours
    water_filled_in_next_two_hours = second_hour_rate * 2

    # Calculate the total amount of water filled in the fourth hour
    water_filled_in_fourth_hour = fourth_hour_rate * 1

    # Calculate the total amount of water filled before the leak
    total_water_filled_before_leak = water_filled_in_first_hour + water_filled_in_next_two_hours + water_filled_in_fourth_hour

    # Calculate the total amount of water lost due to the leak
    total_water_lost_due_to_leak = leak_rate * 1

    # Calculate the remaining amount of water in the pool
    remaining_water = total_water_filled_before_leak - total_water_lost_due_to_leak

    result = remaining_water
    return result

print(solution())