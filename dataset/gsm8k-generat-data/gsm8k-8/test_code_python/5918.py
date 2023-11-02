def solution():
    # Define the variables
    lift_rate = 50
    descend_rate = 10

    # Calculate the elevation during the first 15 minutes of lift
    lift_elevation1 = lift_rate * 15

    # Calculate the elevation during the subsequent 10 minutes of descent
    descend_elevation = descend_rate * 10

    # Calculate the elevation during the second 15 minutes of lift
    lift_elevation2 = lift_rate * 15

    # The highest elevation reached is the sum of the three elevations calculated above
    highest_elevation = lift_elevation1 + lift_elevation2 - descend_elevation
    result = highest_elevation
    return result

print(solution())