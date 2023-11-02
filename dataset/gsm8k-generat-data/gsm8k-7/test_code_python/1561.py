def solution():
    num_notebooks = 4
    num_stamps_per_notebook = 20
    num_binders = 2
    num_stamps_per_binder = 50
    keep_fraction = 1/4

    # Calculate the total number of stamps in the notebooks
    total_notebook_stamps = num_notebooks * num_stamps_per_notebook

    # Calculate the total number of stamps in the binders
    total_binder_stamps = num_binders * num_stamps_per_binder

    # Calculate the total number of stamps that Marie decides to keep
    total_kept_stamps = (total_notebook_stamps + total_binder_stamps) * keep_fraction

    # Calculate the total number of stamps that Marie can give away
    total_given_away_stamps = (total_notebook_stamps + total_binder_stamps) - total_kept_stamps
    result = total_given_away_stamps
    return result

print(solution())