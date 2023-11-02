def solution():
    
    initial_width = 50
    final_width = 80
    width_increase_per_meter = 0.2
    distance_to_cover = (final_width - initial_width) / width_increase_per_meter
    time_taken = distance_to_cover / 5
    result = time_taken
    return result

print(solution())