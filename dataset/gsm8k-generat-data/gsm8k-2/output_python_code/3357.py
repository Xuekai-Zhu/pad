def solution():
    """Bob buys nose spray. He buys 10 of them for a "buy one get one free" promotion. They each cost $3. How much does he pay?"""
    spray_price = 3
    total_sprays = 10
    sprays_without_promotion = total_sprays // 2
    total_price = (sprays_without_promotion * spray_price) + (total_sprays - sprays_without_promotion) * 0
    result = total_price
    return result

print(solution())