def solution():
    # Define the number of shooting stars counted by each person
    bridget_count = 14
    reginald_count = bridget_count - 2
    sam_count = reginald_count + 4

    # Calculate the average number of shooting stars
    average_count = (bridget_count + reginald_count + sam_count) / 3

    # Calculate how many more shooting stars Sam counted than the average
    difference = sam_count - average_count
    result = difference
    return result

print(solution())