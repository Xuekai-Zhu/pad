def solution():
    barney_rate = 45
    carrie_rate = 2 * barney_rate
    jerrie_rate = carrie_rate + 5

    barney_time = 1
    carrie_time = 2
    jerrie_time = 3

    # Calculate the total number of sit-ups Barney can perform
    barney_total = barney_rate * barney_time

    # Calculate the total number of sit-ups Carrie can perform
    carrie_total = carrie_rate * carrie_time

    # Calculate the total number of sit-ups Jerrie can perform
    jerrie_total = jerrie_rate * jerrie_time

    # Calculate the combined total number of sit-ups performed
    total = barney_total + carrie_total + jerrie_total
    result = total
    return result

print(solution())