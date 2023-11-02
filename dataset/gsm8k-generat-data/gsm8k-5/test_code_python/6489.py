def solution():
    total_acorns = 210  # The squirrel stashed 210 acorns
    acorns_per_month = total_acorns / 3  # The squirrel divided the acorns into thirds, one for each month
    acorns_left_per_month = 60  # The squirrel took some from each third, leaving 60 acorns for each winter month
    acorns_eaten_per_month = acorns_per_month - acorns_left_per_month  # The squirrel ate some acorns from each third

    # Calculate the total number of acorns the squirrel ate during the three winter months
    total_acorns_eaten = acorns_eaten_per_month * 3

    # Calculate the number of acorns the squirrel has left to eat in the spring
    acorns_left_for_spring = total_acorns - total_acorns_eaten
    result = acorns_left_for_spring
    return result

print(solution())