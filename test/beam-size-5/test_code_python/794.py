def solution():
    # Calculate Billy's earnings
    billy_earnings = 10 * 20  # Billy earns $10 per hour for 20 hours

    # Calculate Billy's earnings after 2 months
    billy_earnings += 10 * 2  # Billy earns $10 per hour for 20 hours

    # Calculate Billy's earnings after 2 months
    billy_earnings += 1.5 * 20  # Sally earns $1.50 per hour for 20 hours

    # Calculate Sally's earnings
    sally_earnings = 1.5 * 20  # Sally's starting salary is $0.50 more per hour than Billy's starting salary

    # Calculate the difference in earnings between Billy and Sally
    earnings_difference = billy_earnings - sally_earnings
    result = earnings_difference
    return result

print(solution())