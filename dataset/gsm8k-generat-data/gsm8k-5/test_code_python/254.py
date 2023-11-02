def solution():
    cars_in_section_g = 15 * 10  # Section G has 15 rows with 10 cars each
    cars_in_section_h = 20 * 9  # Section H has 20 rows with 9 cars each
    total_cars = cars_in_section_g + cars_in_section_h  # Total number of cars in both sections

    # Calculate the time taken to walk past every car
    time_per_car = 1 / 11  # Nate walks past 11 cars per minute

    # Calculate the total time Nate spent searching for his car
    total_time = total_cars * time_per_car
    result = total_time
    return result

print(solution())