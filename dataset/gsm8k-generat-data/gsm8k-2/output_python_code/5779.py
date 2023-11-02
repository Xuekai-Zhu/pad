def solution():
    """Travis wants to fly to Australia. The regular tickets cost about $2000. As Travis is a student, he will get a 30% discount on this price. How much does he need to pay for his ticket?"""
    regular_price = 2000
    discount = 0.3
    discounted_price = regular_price * (1 - discount)
    result = discounted_price
    return result

print(solution())