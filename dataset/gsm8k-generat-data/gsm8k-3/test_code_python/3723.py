def solution():
    """Cameron drives at twice the speed of his brother, Chase.  But Danielle drives at three times the speed of Cameron.  If it takes Danielle 30 minutes to travel from Granville to Salisbury, how long, in minutes, will it take Chase to travel from Granville to Salisbury?"""
    # Let's assume that Cameron drives at speed x, then Chase drives at speed x/2, and Danielle drives at speed 3x
    # Distance from Granville to Salisbury is same for all, so let's assume it to be d.
    # Time taken by Danielle to cover d distance is given as 30 minutes, or 0.5 hours
    # Using distance formula: d = speed * time
    # We get: d = 3x * 0.5
    # or x = 2d/3

    # Now we can calculate time taken by Chase to cover d distance
    # Using distance formula: d = speed * time
    # We get: d = (x/2) * t
    # Substituting value of x, we get:
    # d = (2d/3 )/2 * t
    # or t = 3/4 hours, or 45 minutes

    # Display the time taken by Chase to travel from Granville to Salisbury
    result = 45
    return result

print(solution())