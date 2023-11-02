def solution():
    """Five times a week, Onur bikes 250 kilometers a day. His friend Hanil bikes 40 more kilometers of Onur biking distance in a day. What's the total distance the two friends bikes in a week?"""
    # Define the biking distance of Onur and Hanil
    onur_distance = 250
    hanil_distance = onur_distance + 40

    # Calculate the weekly biking distance of Onur and Hanil
    weekly_distance = (onur_distance + hanil_distance) * 5

    # Return the result
    result = weekly_distance
    return result

print(solution())