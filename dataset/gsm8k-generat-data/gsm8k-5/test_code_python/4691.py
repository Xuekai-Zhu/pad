def solution():
    # Calculate the time taken to fix the kitchen counter
    kitchen_counter_time = 3 * 8  # Three times longer than painting the house

    # Calculate the total time taken
    total_time = 8 + 6 + kitchen_counter_time

    # Calculate the total amount charged
    total_charge = total_time * 15  # $15 per hour of work

    result = total_charge
    return result

print(solution())