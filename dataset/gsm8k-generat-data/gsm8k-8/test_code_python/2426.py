def solution():
    # Define Wendy's scholarship amount
    wendy_amount = 20000

    # Calculate Kelly's scholarship amount
    kelly_amount = 2 * wendy_amount

    # Calculate Nina's scholarship amount
    nina_amount = kelly_amount - 8000

    # Calculate the total scholarship amount
    total_amount = wendy_amount + kelly_amount + nina_amount
    result = total_amount
    return result

print(solution())