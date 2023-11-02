def solution():
    """Jerry mows 8 acres of lawn each week. He mows ¾ of it with a riding mower that can cut 2 acres an hour. He mows the rest with a push mower that can cut 1 acre an hour. How long does Jerry mow each week?"""
    total_acres = 8
    riding_mower_percentage = 0.75
    push_mower_percentage = 0.25
    riding_mower_acres = total_acres * riding_mower_percentage
    push_mower_acres = total_acres * push_mower_percentage
    riding_mower_time = riding_mower_acres / 2
    push_mower_time = push_mower_acres / 1
    total_time = riding_mower_time + push_mower_time
    result = total_time
    return result

print(solution())