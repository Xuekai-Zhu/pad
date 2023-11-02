def solution():
    # Calculate the total number of apples
    total_apples = 20 + 60 + 40

    # Calculate the average number of apples per person
    average_apples = total_apples / 3

    # Calculate how many times Jim's number of apples can fit into the average
    times_jims_apples_fit = average_apples // 20

    result = times_jims_apples_fit
    return result

print(solution())