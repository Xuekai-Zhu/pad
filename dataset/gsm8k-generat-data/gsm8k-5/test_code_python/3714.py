def solution():
    total_cost = 5000  # Jacoby needs $5000 total for his trip to Brickville

    # Calculate the money Jacoby earns from his job
    job_money = 20 * 10

    # Calculate the money Jacoby earns from selling cookies
    cookie_money = 4 * 24

    # Calculate the total amount of money Jacoby has
    total_money = job_money + cookie_money + 500 + 500

    # Calculate the remaining amount of money Jacoby needs
    remaining_money = total_cost - total_money
    result = remaining_money
    return result

print(solution())