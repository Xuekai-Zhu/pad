def solution():
    """Gretchen read that you should spend 10 minutes walking for every 90 minutes you spend sitting. If Gretchen spends 6 hours working at her desk, how long will she spend walking?"""
    sitting_time = 6 * 60 # convert hours to minutes
    walking_time = sitting_time // 90 * 10
    result = walking_time
    
    return result

print(solution())