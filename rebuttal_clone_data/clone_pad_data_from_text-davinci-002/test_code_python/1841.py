def solution():
    initial_dimes = 30
    initial_nickels = 140
    quarters_from_dimes = initial_dimes / 3
    quarters_from_nickels = initial_nickels / 7
    total_quarters = quarters_from_dimes + quarters_from_nickels
    total_dollars = total_quarters * 0.25
    result = total_dollars
    return result

print(solution())