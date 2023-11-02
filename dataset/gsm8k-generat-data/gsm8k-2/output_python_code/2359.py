def solution():
    """A department store offers a 10% discount for the amount exceeding $100 of the customer's total charge. Jaco bought a pair of shoes for $74; 2 pairs of socks that cost $2 per pair; a bag that costs $42. How much will Jaco pay for those items?"""
    shoes_price = 74
    socks_price = 2 * 2
    bag_price = 42
    total_price = shoes_price + socks_price + bag_price
    discount_threshold = 100

    if total_price > discount_threshold:
        discount_amount = 0.1 * (total_price - discount_threshold)
        total_price -= discount_amount

    result = total_price
    return result

print(solution())