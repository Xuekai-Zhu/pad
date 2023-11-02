def solution():
    # Calculate the number of rotations Jeremy drives in a month
    miles_per_month = 400
    rotations_per_tire = miles_per_month / 725

    # Calculate the total number of rotations Jeremy drives in a month
    total_rotations_per_month = rotations_per_tire * 12

    # Calculate the number of years before the tire needs to be replaced
    years_before_tire = total_rotations_per_month / 12
    result = years_before_tire
    return result

print(solution())