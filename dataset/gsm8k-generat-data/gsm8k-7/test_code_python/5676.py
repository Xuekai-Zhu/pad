def solution():
    don_rate = 3
    ken_rate = don_rate + 2
    laura_rate = ken_rate * 2
    kim_rate = laura_rate - 3

    time_in_minutes = 15

    # Calculate the total number of tiles that Don can paint in 15 minutes
    don_tiles = don_rate * time_in_minutes

    # Calculate the total number of tiles that Ken can paint in 15 minutes
    ken_tiles = ken_rate * time_in_minutes

    # Calculate the total number of tiles that Laura can paint in 15 minutes
    laura_tiles = laura_rate * time_in_minutes

    # Calculate the total number of tiles that Kim can paint in 15 minutes
    kim_tiles = kim_rate * time_in_minutes

    # Calculate the total number of tiles painted by all four people in 15 minutes
    total_tiles = don_tiles + ken_tiles + laura_tiles + kim_tiles
    result = total_tiles
    return result

print(solution())