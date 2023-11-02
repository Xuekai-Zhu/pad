def solution():
    """Maggie spent a quarter of her money, while Riza spent one-third of her money. They each had $60. How much money do the two of them have left?"""
    maggie_spent = 60
    riza_spent = 60
    maggie_left = (1 - 0.25) * maggie_spent
    riza_left = (1 - (1/3)) * riza_spent
    total_left = maggie_left + riza_left
    result = total_left
    return result

print(solution())