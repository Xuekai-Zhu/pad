def solution():
    num_pandas = 16
    percent_pregnant = 0.25

    # Calculate the number of panda couples that get pregnant
    num_pregnant_couples = num_pandas / 2 * percent_pregnant

    # Calculate the total number of panda babies born
    num_babies = num_pregnant_couples * 1

    result = num_babies
    return result

print(solution())