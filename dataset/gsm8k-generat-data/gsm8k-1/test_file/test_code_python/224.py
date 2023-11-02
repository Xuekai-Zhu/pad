def solution():
    """Kalinda is working on a 360 piece puzzle with her mom. Kalinda can normally add 4 pieces per minute. Her mom can typically place half as many pieces per minute as Kalinda. How many hours will it take them to complete this puzzle?"""
    puzzle_size = 360
    kalinda_rate = 4
    mom_rate = kalinda_rate / 2
    combined_rate = kalinda_rate + mom_rate
    minutes_to_complete = puzzle_size / combined_rate
    hours_to_complete = minutes_to_complete / 60
    result = hours_to_complete
    return result

print(solution())