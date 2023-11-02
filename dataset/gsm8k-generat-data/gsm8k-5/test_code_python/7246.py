def solution():
    paul_prays = 20 * 6 + 40  # Pastor Paul prays 20 times per day except on Sunday when he prays twice as much
    bruce_prays = (20 * 6 + 40) / 2  # Pastor Bruce prays half as much as Paul, except on Sunday, when he prays twice as much

    # Calculate the difference in the number of times each pastor prays in a week
    prayers_diff = paul_prays - bruce_prays
    result = prayers_diff
    return result

print(solution())