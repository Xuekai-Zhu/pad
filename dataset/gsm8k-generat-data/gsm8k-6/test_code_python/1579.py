def solution():
    # calculate the total time the phone would last on a full charge
    total_time = 10 * 2

    # calculate the time Olive charged her phone for
    charged_time = 3/5 * 10

    # calculate the total time the phone would last after being charged for the given time
    remaining_time = charged_time * 2

    result = remaining_time
    return result

print(solution())