def solution():
    """James supercharges his car which increases his car's speed by 30%.  He then cuts weight by 15% which increases the speed a further 10 mph.  If his car's original speed was 150 mph what is the new speed?"""
    # Define the original speed and the speed increase percentages
    original_speed = 150
    supercharge_percentage = 0.3
    weight_reduction_percentage = 0.15

    # Calculate the speed increase due to supercharging
    supercharged_speed = original_speed * (1 + supercharge_percentage)

    # Calculate the speed increase due to weight reduction
    weight_reduced_speed = supercharged_speed + 10

    # Calculate the final speed after weight reduction
    final_speed = weight_reduced_speed / (1 - weight_reduction_percentage)

    # Display the final speed
    result = final_speed
    return result

print(solution())