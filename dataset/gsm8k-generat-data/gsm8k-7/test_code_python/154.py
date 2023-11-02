def solution():
    daniella_starting_amt = 400
    ariella_starting_amt = daniella_starting_amt + 200
    ariella_interest_rate = 0.1
    time_period = 2  # in years

    # Calculate the amount of interest earned by Ariella
    ariella_interest = ariella_starting_amt * ariella_interest_rate * time_period

    # Calculate the total amount of money Ariella will have after two years
    ariella_total = ariella_starting_amt + ariella_interest
    result = ariella_total
    return result

print(solution())