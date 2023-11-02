def solution():
    # Convert 50 feet to inches
    total_height_inches = 50 * 12

    # Calculate the number of rungs needed
    num_rungs = int(total_height_inches / 6)

    # Calculate the total length of wood needed for the rungs
    total_length_inches = num_rungs * 18

    # Convert the total length back to feet
    total_length_feet = total_length_inches / 12
    result = total_length_feet
    return result

print(solution())