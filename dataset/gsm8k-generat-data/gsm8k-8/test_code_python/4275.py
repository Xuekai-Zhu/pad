def solution():
    # Define Ken's funds
    ken_funds = 600

    # Calculate Mary's and Scott's funds
    mary_funds = 5 * ken_funds
    scott_funds = mary_funds / 3

    # Calculate the total funds raised
    total_funds = ken_funds + mary_funds + scott_funds

    # Calculate the amount exceeded the goal
    exceeded_amount = total_funds - 4000
    result = exceeded_amount
    return result

print(solution())