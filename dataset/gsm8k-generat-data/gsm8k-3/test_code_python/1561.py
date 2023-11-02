def solution():
    """Marie has 4 notebooks with 20 stamps each. She also has two binders with 50 stamps each. If she decides to only keep 1/4 of the stamps, how many stamps can she give away?"""
    # Calculate the total number of stamps Marie has
    notebooks = 4
    notebook_stamps = 20
    binders = 2
    binder_stamps = 50

    total_stamps = (notebooks * notebook_stamps) + (binders * binder_stamps)

    # Calculate the number of stamps Marie wants to keep
    keep_stamps = total_stamps // 4

    # Calculate the number of stamps Marie can give away
    giveaway_stamps = total_stamps - keep_stamps

    # Display the number of stamps Marie can give away
    result = giveaway_stamps
    return result

print(solution())