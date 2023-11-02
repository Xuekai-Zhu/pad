def solution():
    sandwiches_per_3_days = 2 + 4 + 8  # Paul eats 2 sandwiches on day 1, 4 on day 2, and 8 on day 3
    days_per_cycle = 3  # Paul eats the same number of sandwiches every 3 days
    cycles = 2  # Paul studies for 6 days, so he completes 2 cycles of 3 days each

    # Calculate the total number of sandwiches Paul will eat in 6 days
    total_sandwiches = sandwiches_per_3_days * (cycles + 1)

    result = total_sandwiches
    return result

print(solution())