def solution():
    logs_per_day = 5  # Bart burns 5 logs per day
    days = 120  # November 1 to February 28 is 120 days
    logs_needed = logs_per_day * days  # Bart needs this many logs for the entire season

    # Calculate the number of trees Bart needs to cut down
    trees_needed = logs_needed / 75
    result = trees_needed
    return result

print(solution())