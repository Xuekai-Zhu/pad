def solution():
    """At his cafe, Milton sells apple pie and peach pie slices. He cuts the apple pie into 8 slices. He cuts the peach pie into 6 slices. On the weekend, 56 customers ordered apple pie slices and 48 customers ordered peach pie slices. How many pies did Milton sell during the weekend?"""
    # Calculate the total number of apple pie slices sold
    apple_slices = 56 * 1
    apple_pies = apple_slices / 8

    # Calculate the total number of peach pie slices sold
    peach_slices = 48 * 1
    peach_pies = peach_slices / 6

    # Calculate the total number of pies sold
    total_pies = apple_pies + peach_pies

    result = total_pies
    return result

print(solution())