def solution():
    
    tiffany_blocks = 6
    tiffany_time = 3
    moses_blocks = 12
    moses_time = 8
    tiffany_speed = tiffany_blocks / tiffany_time
    moses_speed = moses_blocks / moses_time
    result = max(tiffany_speed, moses_speed)
    return result

print(solution())