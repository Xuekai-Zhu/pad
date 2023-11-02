def solution():
    """Honey earned $80 a day. Every day, she spent part of her pay and saved the rest. After 20 days of work, she spent $1360. How much did Honey save in 20 days?"""
    # Calculate the total earnings in 20 days
    total_earnings = 80 * 20

    # Calculate the total amount spent in 20 days
    total_spent = 1360

    # Calculate the amount saved in 20 days
    amount_saved = total_earnings - total_spent

    # return the result
    result = amount_saved
    return result

print(solution())