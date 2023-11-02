def solution():
    """Diane is playing poker with her friends and is not having very good luck. She starts with $100 and wins 5 hands for a total of $65 dollars to add to her $100. Emboldened, she begins betting bigger and riskier and ends up losing all her money and owing her friends $50. How much money did Diane lose in all?"""
    initial_money = 100
    total_winnings = 65
    final_money = initial_money + total_winnings - 50
    total_loss = initial_money - final_money
    result = total_loss
    return result

print(solution())