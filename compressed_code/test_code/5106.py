def solution():
    
    camila_hikes = 7
    amanda_hikes = 8 * camila_hikes
    steven_hikes = amanda_hikes + 15
    weeks_to_equal = (steven_hikes - camila_hikes) / 4
    result = weeks_to_equal
    return result

print(solution())