def solution():
    # Define Jacoby's earnings from his job
    job_earnings = 20 * 10

    # Define Jacoby's earnings from selling cookies
    cookie_earnings = 24 * 4

    # Calculate Jacoby's total earnings
    total_earnings = job_earnings + cookie_earnings

    # Subtract the cost of the lottery ticket and add the money from his sisters
    total_funds = total_earnings - 10 + 500 + 500

    # Calculate how much more Jacoby needs to save
    remaining_cost = 5000 - total_funds

    result = remaining_cost
    return result

print(solution())