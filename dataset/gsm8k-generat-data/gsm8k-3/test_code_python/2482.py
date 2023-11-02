def solution():
    """Jenna is hemming her prom dress. The dress's hem is 3 feet long. Each stitch Jenna makes is 1/4 inch long. If Jenna makes 24 stitches per minute, how many minutes does it take Jenna to hem her dress?"""
    # Convert the length of the hem to inches
    hem_length = 3 * 12

    # Calculate the number of stitches Jenna needs to make
    num_stitches = hem_length / 0.25

    # Calculate the number of minutes it takes Jenna to make all the stitches
    minutes = num_stitches / 24

    # Display the number of minutes Jenna takes to hem her dress
    result = minutes
    return result

print(solution())