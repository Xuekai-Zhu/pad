def solution():
    """Marie has 4 notebooks with 20 stamps each. She also has two binders with 50 stamps each. If she decides to only keep 1/4 of the stamps, how many stamps can she give away?"""
    notebook_stamps = 4 * 20
    binder_stamps = 2 * 50
    total_stamps = notebook_stamps + binder_stamps
    keep_stamps = total_stamps / 4
    give_away_stamps = total_stamps - keep_stamps
    result = give_away_stamps
    return result

print(solution())