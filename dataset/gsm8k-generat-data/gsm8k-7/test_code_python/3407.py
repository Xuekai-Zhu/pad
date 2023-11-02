def solution():
    peter_distance = 2 + 3  # Peter runs 3 miles more than Andrew's 2 miles
    andrew_distance = 2
    num_days = 5

    # Calculate the total distance Peter has run in 5 days
    total_peter_distance = peter_distance * num_days

    # Calculate the total distance Andrew has run in 5 days
    total_andrew_distance = andrew_distance * num_days

    # Calculate the total distance both have run in 5 days
    total_distance = total_peter_distance + total_andrew_distance
    result = total_distance
    return result

print(solution())