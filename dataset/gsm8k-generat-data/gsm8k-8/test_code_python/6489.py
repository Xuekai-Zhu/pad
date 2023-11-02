def solution():
    # Define the total number of acorns and the number of acorns left for each winter month
    total_acorns = 210
    acorns_per_month = 60

    # Calculate the number of acorns the squirrel took from each third
    acorns_taken = (3 * acorns_per_month) - total_acorns

    # Calculate the number of acorns left in each third after the squirrel took some
    acorns_per_third = (total_acorns - acorns_taken) / 3

    # Calculate the number of acorns the squirrel combined to eat in the spring
    acorns_combined = 3 * (acorns_per_third - acorns_per_month)

    result = acorns_combined
    return result

print(solution())