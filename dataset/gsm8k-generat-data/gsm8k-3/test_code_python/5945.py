def solution():
    """Milly is making croissants. She needs to fold the dough 4 times, which takes 5 minutes each time, then let it rest for 75 minutes each time. If mixing the ingredients takes 10 minutes and baking the croissants takes 30 minutes, how many hours does the whole process take?"""
    # Calculate total time for folding and resting the dough
    folding_time = 4 * 5  # 4 times folding, each time takes 5 minutes
    resting_time = 4 * 75  # 4 times resting, each time takes 75 minutes
    dough_time = folding_time + resting_time

    # Calculate total time for the whole process
    total_time = dough_time + 10 + 30  # Mixing ingredients for 10 minutes, baking for 30 minutes

    # Convert total time to hours
    total_time_hours = total_time / 60

    # Display the total time in hours
    result = total_time_hours
    return result

print(solution())