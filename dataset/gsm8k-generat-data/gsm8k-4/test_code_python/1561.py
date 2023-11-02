def solution():
    """Marie has 4 notebooks with 20 stamps each. She also has two binders with 50 stamps each. If she decides to only keep 1/4 of the stamps, how many stamps can she give away?"""
    # Define the number of stamps in each notebook and binder
    notebook_stamps = 20
    binder_stamps = 50

    # Calculate the total number of stamps 
    total_stamps = notebook_stamps * 4 + binder_stamps * 2

    # Calculate the number of stamps Marie will keep
    kept_stamps = total_stamps / 4

    # Calculate the number of stamps that Marie can give away
    given_away_stamps = total_stamps - kept_stamps

    # Return the result
    result = given_away_stamps
    return result

print(solution())