def solution():
    """Carol spends 4 hours writing a song, half that much time recording it, and 90 minutes editing it. What percentage of her total work time did she spend editing?"""
    
    writing_time = 4
    recording_time = writing_time / 2
    editing_time = 1.5
    total_time = writing_time + recording_time + editing_time
    percentage = (editing_time / total_time) * 100
    
    return percentage

print(solution())