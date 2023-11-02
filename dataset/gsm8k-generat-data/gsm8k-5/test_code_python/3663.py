def solution():
    # Let's call Beth's current amount 'x'
    x = 0
    while True:
        if ((x + 35) == 105) and ((x - 10) == (x + 35)):
            beth = x + 35  # Beth's amount is x + $35
            jan = x - 10  # Jan's amount is x - $10
            total_amount = beth + jan
            result = total_amount
            return result
        x += 1  # Increment x until we find the solution

print(solution())