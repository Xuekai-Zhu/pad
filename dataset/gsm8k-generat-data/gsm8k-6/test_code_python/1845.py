def solution():
    # Calculate the cost of buying 4 CDs of each type
    total_cost = 4*(5 + 10 + 3 + 7)  # rock and roll, pop, dance, and country CDs

    # Calculate the difference between the total cost and Julia's budget
    money_short = total_cost - 75

    result = money_short
    return result

print(solution())