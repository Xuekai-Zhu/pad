def solution():
    # Calculate the total amount paid to minor characters
    total_paid_minor = 4 * 15000

    # Calculate the total amount paid to major characters
    total_paid_major = 5 * 3 * 15000

    # Calculate the total amount paid per episode
    total_paid = total_paid_minor + total_paid_major

    result = total_paid
    return result

print(solution())