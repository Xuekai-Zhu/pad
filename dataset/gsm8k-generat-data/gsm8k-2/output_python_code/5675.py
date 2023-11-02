def solution():
    """Don can paint 3 tiles a minute, Ken can paint 2 more tiles a minute than Don and Laura can paint twice as many tiles as Ken. Kim can paint 3 fewer tiles than Laura can in a minute. How many tiles can Don, Ken, Laura and Kim paint in 15 minutes?"""
    don_speed = 3
    ken_speed = don_speed + 2
    ken_paints = ken_speed * 15
    laura_paints = ken_paints * 2
    kim_paints = laura_paints - 3
    total_tiles = (don_speed + ken_speed + laura_paints + kim_paints) * 15
    result = total_tiles
    return result

print(solution())