def solution():
    """Jenna is hemming her prom dress. The dress's hem is 3 feet long. Each stitch Jenna makes is 1/4 inch long. If Jenna makes 24 stitches per minute, how many minutes does it take Jenna to hem her dress?"""
    hem_length = 3 * 12 # convert feet to inches
    stitch_length = 1/4
    stitches_needed = hem_length / stitch_length
    stitches_per_minute = 24
    time_needed = stitches_needed / stitches_per_minute
    result = time_needed
    return result

print(solution())