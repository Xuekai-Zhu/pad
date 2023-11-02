def solution():
    clean_and_jerk = 80
    snatch = 50

    # Double the clean and jerk weight and increase the snatch weight by 80%
    clean_and_jerk *= 2
    snatch *= 1.8

    # Calculate the new combined lifting capacity
    new_total = clean_and_jerk + snatch
    result = new_total
    return result

print(solution())