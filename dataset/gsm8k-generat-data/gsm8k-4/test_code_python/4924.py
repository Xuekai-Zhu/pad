def solution():
    """Diane is playing poker with her friends and is not having very good luck. She starts with $100 and wins 5 hands for a total of $65 dollars to add to her $100. Emboldened, she begins betting bigger and riskier and ends up losing all her money and owing her friends $50. How much money did Diane lose in all?"""
    # Define the initial amount of money and the amount won in the first 5 hands
    initial_amount = 100
    amount_won = 65

    # Determine the new amount after winning the first 5 hands
    total_amount = initial_amount + amount_won

    # Subtract the amount owed to friends to get the final amount
    final_amount = total_amount - 50

    # Calculate the total amount lost
    total_loss = initial_amount - final_amount

    # Return the result
    result = total_loss
    return result

print(solution())