def solution():
    """Jenna is hemming her prom dress. The dress's hem is 3 feet long. Each stitch Jenna makes is 1/4 inch long. If Jenna makes 24 stitches per minute, how many minutes does it take Jenna to hem her dress?"""
    hem_length = 3 * 12  # convert feet to inches
    stitch_length = 1 / 4
    stitches_per_inch = 1 / stitch_length
    total_stitches = hem_length * stitches_per_inch
    stitch_time = 1 / 24  # minutes per stitch
    total_time = total_stitches * stitch_time
    result = total_time
    return result

print(solution())