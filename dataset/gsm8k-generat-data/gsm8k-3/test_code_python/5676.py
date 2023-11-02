def solution():
    """Don can paint 3 tiles a minute, Ken can paint 2 more tiles a minute than Don and Laura can paint twice as many tiles as Ken. Kim can paint 3 fewer tiles than Laura can in a minute. How many tiles can Don, Ken, Laura and Kim paint in 15 minutes?"""
    
    # Define the number of tiles each person can paint per minute
    don_rate = 3
    ken_rate = don_rate + 2
    laura_rate = ken_rate * 2
    kim_rate = laura_rate - 3
    
    # Calculate the number of tiles each person can paint in 15 minutes
    don_tiles = don_rate * 15
    ken_tiles = ken_rate * 15
    laura_tiles = laura_rate * 15
    kim_tiles = kim_rate * 15
    
    # Calculate the total number of tiles painted by all four people
    total_tiles = don_tiles + ken_tiles + laura_tiles + kim_tiles
    
    # Display the total number of tiles painted
    result = total_tiles
    return result

print(solution())