def solution():
    """James supercharges his car which increases his car's speed by 30%. He then cuts weight by 15% which increases the speed a further 10 mph. If his car's original speed was 150 mph, what is the new speed?"""
    # Define the original speed of the car
    original_speed = 150

    # Calculate the speed increase from supercharging
    supercharge_increase = original_speed * 0.3

    # Calculate the speed increase from cutting weight
    weight_cut_increase = 10

    # Calculate the new speed after supercharging
    supercharge_speed = original_speed + supercharge_increase

    # Calculate the new speed after cutting weight
    weight_cut_speed = supercharge_speed + weight_cut_increase

    # Convert the final speed to an integer
    final_speed = int(weight_cut_speed)

    # Return the result
    result = final_speed
    return result

print(solution())