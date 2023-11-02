def solution():
    # Calculate the total number of acorns the squirrel had initially
    initial_acorns = 3 * 60  # the squirrel divided the pile into thirds and left 60 acorns for each winter month

    # Calculate the total number of acorns the squirrel took for the first two winter months
    winter_acorns = 2 * 60

    # Calculate the number of acorns left for the last winter month
    last_month_acorns = initial_acorns - winter_acorns

    # Add the acorns the squirrel took for the first two winter months
    eaten_acorns = winter_acorns - last_month_acorns

    result = eaten_acorns
    return result

print(solution())