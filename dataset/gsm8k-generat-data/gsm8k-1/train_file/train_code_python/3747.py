def solution():
    """Lucy works in a pet shop. She can clean 2 aquariums in 3 hours. If Lucy is working 24 hours this week, how many aquariums could she clean?"""
    aquariums_per_hours = 2/3
    total_hours_worked = 24
    aquariums_cleaned = aquariums_per_hours * total_hours_worked
    result = aquariums_cleaned
    return result

print(solution())