def solution():
    """At his cafe, Milton sells apple pie and peach pie slices.  He cuts the apple pie into 8 slices.  He cuts the peach pie into 6 slices.  On the weekend, 56 customers ordered apple pie slices and 48 customers ordered peach pie slices.  How many pies did Milton sell during the weekend?"""
    # Define the number of slices per pie for each type of pie
    APPLE_SLICES = 8
    PEACH_SLICES = 6

    # Calculate the number of apple and peach pies sold
    apple_pies = 56 // APPLE_SLICES
    peach_pies = 48 // PEACH_SLICES

    # Display the total number of pies sold
    result = apple_pies + peach_pies
    return result

print(solution())