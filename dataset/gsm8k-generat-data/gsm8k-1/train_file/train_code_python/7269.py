def solution():
    """Bob is tilling a plot of his garden. The plot is 110 feet wide by 120 feet long. His tiller digs a swath two feet wide, and he can till 1 foot of ground in about 2 seconds. How long will it take him to till this plot of land, in minutes?"""
    plot_width = 110
    plot_length = 120
    swath_width = 2
    tilling_rate = 0.5 # 1 foot per 2 seconds = 0.5 feet per second
    total_area = plot_width * plot_length
    tilled_area = (plot_width - swath_width) * (plot_length - swath_width)
    tilling_time = tilled_area / tilling_rate
    time_in_minutes = tilling_time / 60
    result = time_in_minutes
    return result

print(solution())