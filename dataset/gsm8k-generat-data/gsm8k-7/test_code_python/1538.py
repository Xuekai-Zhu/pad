def solution():
    initial_paintings = 2
    num_days = 5

    total_paintings = initial_paintings

    for i in range(1, num_days):
        new_paintings = initial_paintings * (2 ** i)
        total_paintings += new_paintings

    result = total_paintings
    return result

print(solution())