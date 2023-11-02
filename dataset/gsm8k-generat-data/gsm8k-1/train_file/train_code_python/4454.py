def solution():
    """Abigail spent 60% of her money on food, and 25% of the remainder on her phone bill. After spending $20 on entertainment, she is left with $40. How much money did Abigail have initially?"""
    final_amount = 40
    entertainment_spending = 20
    total_spending = final_amount + entertainment_spending

    remaining_amount = total_spending / (1 - 0.25)
    food_spending = remaining_amount * 0.6
    initial_amount = remaining_amount + food_spending

    result = initial_amount
    return result

print(solution())