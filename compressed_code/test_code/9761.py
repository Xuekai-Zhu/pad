def solution():
    
    total_windows = 122
    rooms_with_four = 5
    rooms_with_three = 8
    windows_with_four = rooms_with_four * 4
    windows_with_three = rooms_with_three * 3
    windows_with_two = total_windows - windows_with_four - windows_with_three
    rooms_with_two = windows_with_two / 2
    result = rooms_with_two
    return result

print(solution())