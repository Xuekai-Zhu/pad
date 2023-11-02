def solution():
    ken_funds = 600  # Ken has $600
    mary_funds = 5 * ken_funds  # Mary's collection is 5 times what Ken has
    scott_funds = mary_funds / 3  # Scott's funds are 1/3 of Mary's funds
    total_funds = ken_funds + mary_funds + scott_funds  # Total funds raised by the three

    # Calculate how much the three have exceeded their goal
    excess_funds = total_funds - 4000
    result = excess_funds
    return result

print(solution())