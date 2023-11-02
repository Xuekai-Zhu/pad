def solution():
    """Travis wants to fly to Australia. The regular tickets cost about $2000. As Travis is a student, he will get a 30% discount on this price. How much does he need to pay for his ticket?"""
    regular_price = 2000
    discount_percent = 30
    discount_amount = regular_price * (discount_percent / 100)
    final_price = regular_price - discount_amount
    result = final_price
    return result

print(solution())