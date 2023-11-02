def solution():
    """Bran's tuition fee is $90. He does a part-time job that pays him $15 per month and he has a scholarship that takes care of 30% of his tuition fee. If he needs to pay his tuition fee within 3 months, how much does Bran still need to pay?"""
    # Define the tuition fee and the scholarship percentage
    TUITION_FEE = 90
    SCHOLARSHIP_PERCENTAGE = 0.3

    # Calculate the scholarship amount
    scholarship = TUITION_FEE * SCHOLARSHIP_PERCENTAGE

    # Calculate the remaining tuition fee after the scholarship
    remaining_tuition = TUITION_FEE - scholarship

    # Calculate Bran's earnings from his part-time job for 3 months
    earnings = 15 * 3

    # Calculate the amount still needed to be paid by Bran
    still_due = remaining_tuition - earnings

    # Display the amount still due
    result = still_due
    return result

print(solution())