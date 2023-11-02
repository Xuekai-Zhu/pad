def solution():
    
    total_kids = 20
    first_wave = total_kids / 2
    second_wave = (total_kids - first_wave) / 2
    still_awake = total_kids - first_wave - second_wave
    result = still_awake
    return result

print(solution())