def solution():
    
    current_bunch_size = 9
    current_bunches = 8
    new_bunch_size = 12
    new_bunches = (current_bunch_size * current_bunches) // new_bunch_size
    result = new_bunches
    return result

print(solution())