def solution():
    
    beatrice_width = 2
    beatrice_length = 24
    marcell_width = 3
    marcell_length = 14
    total_rollups = (beatrice_width * beatrice_length) + (marcell_width * marcell_length)
    average_rollups = total_rollups / 2
    result = average_rollups
    return result

print(solution())