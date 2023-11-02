def solution():
    """John's weight bench can support 1000 pounds. He wants to make sure to stay 20% under that weight for safety. If he weighs 250 pounds how much weight can he put on the bar?"""
    # Define the maximum weight the bench can support and the safety factor
    max_weight = 1000
    safety_factor = 0.2

    # Calculate the maximum weight John can lift
    max_lift = (max_weight * (1 - safety_factor)) - 250

    result = max_lift
    return result

print(solution())