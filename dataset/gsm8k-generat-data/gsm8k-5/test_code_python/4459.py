def solution():
    total = 4  # Kendall has a total of $4 in coins
    quarters = 10  # Kendall has 10 quarters
    dimes = 12  # Kendall has 12 dimes

    # Calculate the total value of quarters and dimes
    total_qd = (0.25 * quarters) + (0.1 * dimes)

    # Calculate the value of nickels needed to reach the total
    total_n = total - total_qd
    num_n = total_n / 0.05  # Each nickel has a value of $0.05

    result = num_n
    return result

print(solution())