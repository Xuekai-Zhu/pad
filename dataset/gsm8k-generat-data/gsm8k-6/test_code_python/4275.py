def solution():
    # Find Mary's funds and Scott's funds
    ken_funds = 600
    mary_funds = 5 * ken_funds
    scott_funds = mary_funds / 3

    # Find the total funds raised by the three
    total_funds = ken_funds + mary_funds + scott_funds

    # Find the amount by which they exceeded the goal
    exceeded_amount = total_funds - 4000
    result = exceeded_amount
    return result

print(solution())