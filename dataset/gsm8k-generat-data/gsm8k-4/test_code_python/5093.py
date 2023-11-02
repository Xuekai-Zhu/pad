def solution():
    """Maurice had only been horseback riding a handful of times in his life. His best friend, Matt, goes horseback riding regularly. When Maurice went to visit Matt for two weeks, he rode another 8 times. Each time, Matt went with him. Meanwhile, besides the times that Matt accompanied Maurice, he rode an additional 16 times. If the total number of times Matt rode during that two weeks is three times the number of times Maurice had ridden before his visit, how many times had Maurice been horseback riding before visiting Matt?"""
    # Let x be the number of times Maurice had ridden before his visit
    x = None

    # Calculate the total number of times Matt rode during the two weeks
    total_rides = 8 + 16 + 8*x

    # Calculate x using the information that total_rides is three times the number of times Maurice had ridden before his visit
    x = total_rides / 3 - 8

    result = x
    return result

print(solution())