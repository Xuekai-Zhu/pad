def solution():
    trip_cost = 5000

    # Calculate the amount of money Jacoby earns from his job
    job_income = 20 * 10

    # Calculate the amount of money Jacoby earns from selling cookies
    cookie_income = 4 * 24

    # Calculate the total amount of money Jacoby has after his job and cookie sales
    total_income = job_income + cookie_income

    # Subtract the cost of the lottery ticket and add the lottery winnings and gifts from his sisters
    total_income = total_income - 10 + 500 + 500

    # Calculate how much more money Jacoby needs for the trip
    remaining_cost = trip_cost - total_income
    result = remaining_cost
    return result

print(solution())