def solution():
    # Let's assume Susan had "x" amount of money at first
    # She spent 1/5 of it in September, so she spent (1/5)*x
    # She spent 1/4 of it in October (after spending in September), so she spent (1/4)*(4/5)*x = (1/5)*x
    # She spent $120 in November (after spending in September and October), so she spent a total of (1/5 + 1/5 + 120) = (2/5)*x + 120
    # She still had $540 left after spending, so (3/5)*x - 120 = 540
    # Solving for x, we get x = $1200
    initial_amount = 1200
    result = initial_amount
    return result

print(solution())