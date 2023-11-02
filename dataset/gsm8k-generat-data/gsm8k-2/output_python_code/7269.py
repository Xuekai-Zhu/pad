def solution():
    """Bob is tilling a plot of his garden. The plot is 110 feet wide by 120 feet long. His tiller digs a swath two feet wide, and he can till 1 foot of ground in about 2 seconds. How long will it take him to till this plot of land, in minutes?"""
    width = 110
    length = 120
    swath_width = 2
    tilling_speed = 1 / 2  # in feet per second
    area = width * length
    total_swaths = width // swath_width + 1  # add 1 for partial swath
    time = area * total_swaths / tilling_speed / 60  # in minutes
    result = time
    return result

print(solution())