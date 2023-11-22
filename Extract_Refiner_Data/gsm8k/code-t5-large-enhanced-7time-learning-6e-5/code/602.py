def solution():
    
    # Define the number of rotations per car
    rotations_per_car = 725

    # Define the number of miles driven by Jeremy
    miles_per_month = 400

    # Define the number of rotations per tire
    rotations_per_tire = rotations_per_car * 2

    # Calculate the total number of rotations
    total_rotations = miles_per_month * rotations_per_tire * 12

    # Calculate the number of years before the tire needs to be replaced
    years_before_tire = total_rotations / (10000 / rotations_per_tire)

    # Display the number of years before the tire needs to be replaced
    result = years_before_tire
    return result

print(solution())