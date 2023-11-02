def solution():
    days = 8
    num_builders = 3

    # Calculate the amount of work required to build the cottage
    work_required = num_builders * days

    # Calculate the number of days it would take 6 builders to build the same amount of work
    num_builders_new = 6
    days_new = work_required / (num_builders_new * 1.0)

    result = days_new
    return result

print(solution())