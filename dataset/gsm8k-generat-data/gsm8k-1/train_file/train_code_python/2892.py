def solution():
    """Raine's house is just a walking distance from her school. It takes her 150 steps to walk to the school. How many steps does she take walking to and from school in five days?"""
    steps_to_school = 150
    round_trip_steps = steps_to_school * 2
    days_per_week = 5
    total_steps = round_trip_steps * days_per_week
    result = total_steps
    return result

print(solution())