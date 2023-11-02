def solution():
    # Let x be the number of $20 bills
    x = 0
    while True:
        # Calculate the number of $10 bills
        y = 2*x

        # Calculate the total amount of money
        total_amount = 10*y + 20*x
        if total_amount == 120:
            result = x
            break
        elif total_amount > 120:
            result = "No solution"
            break
        x += 1
    return result

print(solution())