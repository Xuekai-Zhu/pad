def solution():
    balloons = 52
    minutes_to_fill = 10
    minutes_to_fill_half = 5
    minutes_to_fill_two = balloons - minutes_to_fill - minutes_to_fill_half
    result = minutes_to_fill + minutes_to_fill_half + minutes_to_fill_two 
    
    return result

print(solution())