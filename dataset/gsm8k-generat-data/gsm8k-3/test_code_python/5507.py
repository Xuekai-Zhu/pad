def solution():
    """John's weight bench can support 1000 pounds.  He wants to make sure to stay 20% under that weight for safety.  If he weighs 250 pounds how much weight can he put on the bar?"""
    # Define the maximum weight the bench can support and the safety margin
    MAX_WEIGHT = 1000
    SAFETY_MARGIN = 0.2

    # Calculate the maximum weight John can lift
    max_lift_weight = (1 - SAFETY_MARGIN) * MAX_WEIGHT - 250

    # Display the maximum weight John can lift
    result = max_lift_weight
    return result

print(solution())