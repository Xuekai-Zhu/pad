def solution():
    """A department store offers a 10% discount for the amount exceeding $100 of the customer's total charge. Jaco bought a pair of shoes for $74; 2 pairs of socks that cost $2 per pair; a bag that costs $42. How much will Jaco pay for those items?"""
    # Define the prices of the items
    SHOE_PRICE = 74
    SOCK_PRICE = 2
    BAG_PRICE = 42

    # Calculate the total cost of the items
    total_cost = SHOE_PRICE + (2 * SOCK_PRICE) + BAG_PRICE

    # Calculate the discount, if applicable
    if total_cost > 100:
        discount_amount = (total_cost - 100) * 0.1
        total_cost -= discount_amount

    # Display the total cost after discount (if any)
    result = total_cost
    return result

print(solution())