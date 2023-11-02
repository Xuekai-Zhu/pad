def solution():
    # Calculate the total amount saved by Thomas
    thomas_total = 40 * 12 * 6

    # Calculate the amount saved by Joseph per month
    joseph_amount = (3/5) * 40

    # Calculate the total amount saved by Joseph
    joseph_total = joseph_amount * 12 * 6

    # Calculate the total amount saved by both
    total_savings = thomas_total + joseph_total
    result = total_savings
    return result

print(solution())