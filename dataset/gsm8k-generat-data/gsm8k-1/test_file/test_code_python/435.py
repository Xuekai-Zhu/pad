def solution():
    """Wayne and Bernadette are movie stars heading to the premiere of their latest film. Bernadette wants to arrive 5 minutes before Wayne. Wayne is staying at a hotel close to the premiere theater, and Bernadette is staying at her high-rise apartment in the same city. The drive from Bernadette’s apartment takes four times as long as the drive from Wayne’s hotel. If it takes Wayne four minutes to be driven to the theater, how much earlier should Bernadette leave than Wayne to get to the theater first?"""
    wayne_time = 4  # time in minutes
    bernadette_time = wayne_time * 4  # time in minutes
    desired_time_diff = 5  # time difference in minutes
    total_time = wayne_time + desired_time_diff
    bernadette_departure_time = total_time - bernadette_time
    result = bernadette_departure_time
    return result

print(solution())