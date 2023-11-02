def solution():
    cash = 40  # Oliver has $40
    quarters = 200  # Oliver has 200 quarters

    # Oliver gives $5 (20 quarters) and 120 quarters to his sister
    cash -= 5
    quarters -= 120

    # Convert the remaining quarters to dollars
    cash += (quarters * 0.25)

    result = cash
    return result

print(solution())