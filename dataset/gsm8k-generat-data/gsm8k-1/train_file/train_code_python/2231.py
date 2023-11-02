def solution():
    """Adam goes to school every day. On Monday he had 6 lessons of 30 minutes each, 
    and on Tuesday he had 3 lessons of 1 hour each. On Wednesday, Adam spent twice 
    as much time at school as on Tuesday. How much time in total did Adam spend at 
    school during these 3 days, in hours?"""
    monday_lessons = 6
    monday_duration = 30
    tuesday_lessons = 3
    tuesday_duration = 60
    wednesday_duration = tuesday_duration * 2
    
    total_duration = (monday_lessons * monday_duration 
                      + tuesday_lessons * tuesday_duration 
                      + wednesday_duration)
    total_hours = total_duration / 60
    result = total_hours
    return result

print(solution())