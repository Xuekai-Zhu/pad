def solution():
    
    # Define Billy's hourly wage and the hourly wage raise
    BILLY_WAGE = 10
    BILLY_RAISE = 0.5

    # Define Sally's hourly wage and the hourly wage raise
    SLY_WAGE = BILLY_WAGE + 0.5
    SLY_RAISE = BILLY_WAGE + 0.5

    # Calculate Billy's earnings and Sally's earnings
    billy_earnings = BILLY_WAGE * 20
    sally_earnings = SLY_WAGE * 20

    # Calculate the difference in earnings between Billy and Sally
    difference = billy_earnings - sally_earnings

    # Display the difference in earnings
    result = difference
    return result

print(solution())