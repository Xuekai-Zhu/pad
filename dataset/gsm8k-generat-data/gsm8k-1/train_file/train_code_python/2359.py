def solution():
    """A department store offers a 10% discount for the amount exceeding $100 of the customer's total charge. Jaco bought a pair of shoes for $74; 2 pairs of socks that cost $2 per pair; a bag that costs $42. How much will Jaco pay for those items?"""
    shoes_cost = 74
    socks_cost = 2 * 2
    bag_cost = 42
    total_cost = shoes_cost + socks_cost + bag_cost
    discount_threshold = 100
    if total_cost > discount_threshold:
        discount_amount = (total_cost - discount_threshold) * 0.1
        discounted_total = total_cost - discount_amount
        result = discounted_total
    else:
        result = total_cost
    
    return result

print(solution())