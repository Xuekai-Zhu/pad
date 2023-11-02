def solution():
    """Tom and Elizabeth have a competition to climb a hill. Elizabeth takes 30 minutes to climb the hill. Tom takes four times as long as Elizabeth does to climb the hill. How many hours does it take Tom to climb up the hill?"""
    elizabeth_time = 30
    tom_time = elizabeth_time * 4
    total_time_in_minutes = elizabeth_time + tom_time
    total_time_in_hours = total_time_in_minutes / 60
    result = total_time_in_hours
    return result

print(solution())