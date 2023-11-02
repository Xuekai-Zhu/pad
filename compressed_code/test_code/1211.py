def solution():
    
    notebook_stamps = 4 * 20
    binder_stamps = 2 * 50
    total_stamps = notebook_stamps + binder_stamps
    keep_stamps = total_stamps / 4
    give_away_stamps = total_stamps - keep_stamps
    result = give_away_stamps
    return result

print(solution())