def solution():
    total_legos = 400
    legos_per_airplane = 240
    num_airplanes = 2

    # Calculate the total number of legos needed to create both airplanes
    total_airplane_legos = legos_per_airplane * num_airplanes

    # Calculate the number of additional legos needed
    additional_legos_needed = total_airplane_legos - total_legos
    result = additional_legos_needed
    return result

print(solution())