def solution():
    # Calculate the total distance run on the first four days
    jesse_first_four = (2/3)*3 + 10
    mia_first_four = 3*4

    # Calculate the remaining distance to be run by each person
    jesse_remaining = 30 - jesse_first_four
    mia_remaining = 30 - mia_first_four

    # Calculate the average distance each person needs to run over the final three days
    jesse_avg = jesse_remaining / 3
    mia_avg = mia_remaining / 3

    # Calculate the average of their averages
    avg_avg = (jesse_avg + mia_avg) / 2
    result = avg_avg
    return result

print(solution())