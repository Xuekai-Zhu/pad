def solution():
    """Kendy made 2 online bank transactions. She transferred $60 to her mom and half that amount to her sister. As a result, her account now has $100 left in it. How much money was in the account before the transfer?"""
    # Calculate the total amount transferred
    total_transferred = 60 + 30  # Kendy transferred $60 to her mom and half that amount to her sister

    # Calculate the amount in Kendy's account before the transfer
    amount_before_transfer = total_transferred + 100  # Kendy's account now has $100 left in it

    # Display the amount in Kendy's account before the transfer
    result = amount_before_transfer
    return result

print(solution())