def solution():
    # Calculate the total amount of money saved by Thomas in 6 years
    thomas_savings = 40 * 12 * 6

    # Calculate the amount saved by Joseph per month
    joseph_savings = (3/5) * 40

    # Calculate the total amount of money saved by Joseph in 6 years
    joseph_total_savings = joseph_savings * 12 * 6

    # Calculate the total amount of money saved by both of them
    total_savings = thomas_savings + joseph_total_savings
    result = total_savings
    return result

print(solution())