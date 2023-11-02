def solution():
    """John decides to buy new phones for him, his 2 kids, and his wife. Each phone after the first 2 is half price. If the phone price is $600 how much did he pay for them all?"""
    phone_price = 600
    phone_count = 4
    reduced_price_count = phone_count - 2
    total_price = (2 * phone_price) + (reduced_price_count * (0.5 * phone_price))
    result = total_price
    return result

print(solution())