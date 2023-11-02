def solution():
    """The mayor commissioned two artists to paint 50 murals around the city. Once the work was completed, Celina was paid $1,000 more than 4 times the amount Diego got. If the mayor paid the two a total of $50,000, how much did Diego get?"""
    total_murals = 50
    total_payment = 50000
    celina_payment = (total_payment - 1000) / 5
    diego_payment = (total_payment - celina_payment) / 2
    result = diego_payment
    return result

print(solution())