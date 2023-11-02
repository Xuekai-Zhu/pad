def solution():
    """A pickup truck can fill 20 eight gallon water cans (each can filled three quarters of its capacity) in three hours. If each can is filled to full capacity instead, how long, in hours, will it take to fill 25 cans?"""
    cans_per_hour = 20 / 3
    gallons_per_can = 8 * 0.75
    gallons_needed = 25 * 8
    time_needed = gallons_needed / (cans_per_hour * gallons_per_can)
    result = time_needed
    return result

print(solution())