def solution():
    
    total_balloons = 52
    balloon_capacity = 5
    total_air = total_balloons * balloon_capacity
    first_phase_time = 10
    first_phase_rate = 8
    second_phase_time = 5
    second_phase_rate = 0.5 * first_phase_rate
    third_phase_rate = 2
    remaining_air = total_air

    
    air_filled = first_phase_rate * first_phase_time
    remaining_air -= air_filled

    
    air_filled = second_phase_rate * second_phase_time
    remaining_air -= air_filled

    
    third_phase_time = remaining_air / third_phase_rate

    total_time = first_phase_time + second_phase_time + third_phase_time
    result = total_time
    return result

print(solution())