def solution():
    """John adopts a dog. He takes the dog to the groomer, which costs $100. The groomer offers him a 30% discount for being a new customer. How much does the grooming cost?"""
    original_price = 100
    discount_percent = 30
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    result = final_price
    return result

print(solution())