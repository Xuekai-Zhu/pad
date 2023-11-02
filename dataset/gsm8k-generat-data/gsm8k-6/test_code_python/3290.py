def solution():
    # Using the formula: time = (amount of work) / (rate of work)
    # Let's assume cleaning the house is one unit of work

    # If four pugs can do the job in 45 minutes, their rate of work is:
    rate_per_pug = 1 / (4 * 45)  # one-fourth of the job in one minute

    # If 15 pugs work together, their combined rate of work is:
    combined_rate = 15 * rate_per_pug

    # Using the formula: time = (amount of work) / (rate of work)
    # We can solve for time (in minutes) needed for 15 pugs to clean the house:
    time_needed = 1 / combined_rate

    result = time_needed * 60  # converting time to minutes
    return result

print(solution())