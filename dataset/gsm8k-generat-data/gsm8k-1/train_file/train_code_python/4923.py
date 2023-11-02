def solution():
    """Diane is playing poker with her friends and is not having very good luck. She starts with $100 and wins 5 hands for a total of $65 dollars to add to her $100. Emboldened, she begins betting bigger and riskier and ends up losing all her money and owing her friends $50. How much money did Diane lose in all?"""
    initial_money = 100
    money_won = 65
    money_lost = 150
    total_money = initial_money + money_won - money_lost
    result = -1 * total_money
    return result

print(solution())