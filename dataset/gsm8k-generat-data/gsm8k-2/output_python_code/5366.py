def solution():
    """Kate has to fill 52 balloons for the party. Each balloon holds 5 gallons of air. For the first 10 minutes, she can fill the balloons at a rate of 8 gallons of air per minute. For the next five minutes, she fills them at half that rate. After that, she fills the rest of the balloons at a rate of 2 gallons of air per minute. How many minutes will it take her to fill all of the balloons?"""
    total_balloons = 52
    balloon_capacity = 5
    total_air = total_balloons * balloon_capacity
    first_phase_time = 10
    first_phase_rate = 8
    second_phase_time = 5
    second_phase_rate = 0.5 * first_phase_rate
    third_phase_rate = 2
    remaining_air = total_air

    # First Phase
    air_filled = first_phase_rate * first_phase_time
    remaining_air -= air_filled

    # Second Phase
    air_filled = second_phase_rate * second_phase_time
    remaining_air -= air_filled

    # Third Phase
    third_phase_time = remaining_air / third_phase_rate

    total_time = first_phase_time + second_phase_time + third_phase_time
    result = total_time
    return result

print(solution())