def solution():
    # Calculate the total seminar fee without discount
    seminar_fee = 150 * 10  # 10 teachers registered for the seminar

    # Calculate the total discount if they registered 2 days before the scheduled seminar
    discount = 0.05 * seminar_fee

    # Calculate the total seminar fee with discount
    seminar_fee -= discount

    # Calculate the total cost with food allowance
    total_cost = seminar_fee + (10 * 10)  # $10 food allowance for each teacher

    result = total_cost
    return result

print(solution())