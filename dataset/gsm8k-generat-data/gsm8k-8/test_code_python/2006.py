def solution():
    # Define initial membership fee and rate of increase
    initial_fee = 80
    increase_rate = 10

    # Calculate membership fee for sixth year
    sixth_year_fee = initial_fee + (5 * increase_rate)
    result = sixth_year_fee
    return result

print(solution())