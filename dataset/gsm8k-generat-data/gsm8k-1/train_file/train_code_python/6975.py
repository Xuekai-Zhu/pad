def solution():
    """Each week Carina puts 20 more seashells in a jar than she did the week before. If there are 50 seashells in the jar this week, how many will there be in a month?"""
    current_week_shells = 50
    week_increase = 20
    total_shells = current_week_shells
    
    for i in range(1, 4): #assuming a month has 4 weeks
        new_week_shells = current_week_shells + week_increase
        total_shells += new_week_shells
        current_week_shells = new_week_shells
        
    result = total_shells
    return result

print(solution())