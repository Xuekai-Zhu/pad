def solution():
    wax_for_car = 3
    wax_for_suv = 4
    total_wax_bottle = 11
    wax_spilled = 2

    # Calculate the total wax needed for both vehicles
    total_wax_needed = wax_for_car + wax_for_suv

    # Calculate the total wax left after spilling and detailing both vehicles
    total_wax_left = total_wax_bottle - wax_spilled - total_wax_needed
    result = total_wax_left
    return result

print(solution())