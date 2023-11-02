def solution():
    num_customers = 14
    num_eggs_per_plate = 2
    num_bacon_per_plate = num_eggs_per_plate * 2

    # Calculate the total number of bacon strips needed for all plates
    total_bacon_needed = num_customers * num_bacon_per_plate
    result = total_bacon_needed
    return result

print(solution())