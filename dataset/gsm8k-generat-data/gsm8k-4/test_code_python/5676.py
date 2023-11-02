def solution():
    """Don can paint 3 tiles a minute, Ken can paint 2 more tiles a minute than Don and Laura can paint twice as many tiles as Ken. Kim can paint 3 fewer tiles than Laura can in a minute. How many tiles can Don, Ken, Laura and Kim paint in 15 minutes?"""
    # Define the painting rates of Don, Ken, Laura, and Kim in tiles per minute
    don_rate = 3
    ken_rate = don_rate + 2
    ken_double_rate = ken_rate * 2
    laura_rate = ken_double_rate
    kim_rate = laura_rate - 3

    # Calculate the total number of tiles painted by each person in 15 minutes
    don_total = don_rate * 15
    ken_total = ken_rate * 15
    laura_total = laura_rate * 15
    kim_total = kim_rate * 15

    # Return the result as a dictionary
    result = {
        "Don": don_total,
        "Ken": ken_total,
        "Laura": laura_total,
        "Kim": kim_total
    }
    return result

print(solution())