def solution():
    """Adam goes to school every day. On Monday he had 6 lessons of 30 minutes each, and on Tuesday he had 3 lessons of 1 hour each. On Wednesday, Adam spent twice as much time at school as on Tuesday. How much time in total did Adam spend at school during these 3 days, in hours?"""
    monday_time = 6 * 30 / 60  # in hours
    tuesday_time = 3 * 1  # in hours
    wednesday_time = 2 * tuesday_time  # in hours
    total_time = monday_time + tuesday_time + wednesday_time
    result = total_time
    return result

print(solution())