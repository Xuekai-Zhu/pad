def solution():
    """Jenna is hemming her prom dress. The dress's hem is 3 feet long. Each stitch Jenna makes is 1/4 inch long. If Jenna makes 24 stitches per minute, how many minutes does it take Jenna to hem her dress?"""
    # Define the length of the hem in inches
    hem_length_inches = 3 * 12

    # Define the length of each stitch in inches
    stitch_length_inches = 1/4

    # Calculate the number of stitches needed to hem the entire dress
    total_stitches = hem_length_inches / stitch_length_inches

    # Calculate the time needed to hem the dress in minutes
    minutes_needed = total_stitches / 24

    # Return the result
    result = minutes_needed
    return result

print(solution())