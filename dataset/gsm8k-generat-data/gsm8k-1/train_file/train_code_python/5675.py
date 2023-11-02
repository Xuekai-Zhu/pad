def solution():
    """Don can paint 3 tiles a minute, Ken can paint 2 more tiles a minute than Don and Laura can paint twice as many tiles as Ken. Kim can paint 3 fewer tiles than Laura can in a minute. How many tiles can Don, Ken, Laura and Kim paint in 15 minutes?"""
    don_speed = 3
    ken_speed = don_speed + 2
    laura_speed = ken_speed * 2
    kim_speed = laura_speed - 3
    total_time = 15
    don_tiles = don_speed * total_time
    ken_tiles = ken_speed * total_time
    laura_tiles = laura_speed * total_time
    kim_tiles = kim_speed * total_time
    total_tiles = don_tiles + ken_tiles + laura_tiles + kim_tiles
    result = total_tiles
    return result

print(solution())