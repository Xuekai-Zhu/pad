def solution():
    """Each week Carina puts 20 more seashells in a jar than she did the week before. If there are 50 seashells in the jar this week, how many will there be in a month?"""
    current_seashells = 50
    seashells_added_per_week = 20
    total_seashells = current_seashells
    for i in range(1, 4):
        current_seashells += seashells_added_per_week
        total_seashells += current_seashells
    result = total_seashells
    return result

print(solution())