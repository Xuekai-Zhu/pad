def solution():
    
    switch_points = 2000
    bunny_points = 8 * 100
    total_points = bunny_points

    snickers_points = 25
    snickers_needed = (switch_points - total_points) // snickers_points

    result = snickers_needed
    return result

print(solution())