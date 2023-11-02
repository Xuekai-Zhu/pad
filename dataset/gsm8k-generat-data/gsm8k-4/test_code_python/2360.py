def solution():
    """A department store offers a 10% discount for the amount exceeding $100 of the customer's total charge. Jaco bought a pair of shoes for $74; 2 pairs of socks that cost $2 per pair; a bag that costs $42. How much will Jaco pay for those items?"""
    # Calculate the total cost of Jaco's purchase
    total_cost = 74 + (2 * 2) + 42

    # Calculate the amount exceeding $100
    excess_amount = max(total_cost - 100, 0)

    # Calculate the discount amount
    discount = excess_amount * 0.1

    # Calculate the total amount to be paid by Jaco
    total_payment = total_cost - discount

    result = total_payment
    return result

print(solution())