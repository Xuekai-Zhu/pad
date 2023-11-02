def solution():
    """Shara borrowed money from her brother 6 months ago. She returned $10 per month to her brother. Currently, she was able to return half of the money she borrowed. How much will she still owe her brother 4 months from now?"""
    # Define the amount of money borrowed by Shara
    total_borrowed = 6 * 10  # $10 returned per month for 6 months

    # Calculate the amount of money returned by Shara
    total_returned = 5 * 10  # Shara returned $10 per month for 5 months

    # Calculate the remaining amount owed by Shara
    remaining_amount = total_borrowed - total_returned

    # Calculate the amount that Shara will still owe in 4 months
    remaining_amount_in_4_months = remaining_amount - (4 * 10)  # $10 returned per month for 4 months

    # Display the remaining amount that Shara will owe in 4 months
    result = remaining_amount_in_4_months
    return result

print(solution())