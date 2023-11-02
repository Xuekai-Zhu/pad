def solution():
    # Calculate the money Jacoby earned from his job
    job_money = 20 * 10  # Jacoby works 10 hours and earns $20 per hour

    # Calculate the money Jacoby earned from selling cookies
    cookie_money = 4 * 24  # Jacoby sells 24 pieces of cookies for $4 each

    # Calculate the total money Jacoby has after buying a lottery ticket and receiving money from his sisters
    total_money = job_money + cookie_money - 10 + 500 + 500

    # Calculate the amount of money Jacoby still needs for his trip
    needed_money = 5000 - total_money
    result = needed_money
    return result

print(solution())