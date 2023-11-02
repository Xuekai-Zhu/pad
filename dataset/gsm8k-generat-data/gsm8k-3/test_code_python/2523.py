def solution():
    """Jim buys a wedding ring for $10,000.  He gets his wife a ring that is twice that much and sells the first one for half its value.  How much is he out of pocket?"""
    # Define the cost of the wedding ring
    wedding_ring_cost = 10000

    # Calculate the cost of the second ring
    second_ring_cost = 2 * wedding_ring_cost

    # Calculate the amount Jim receives from selling the first ring
    first_ring_sale = wedding_ring_cost / 2

    # Calculate Jim's total out of pocket expense
    total_cost = wedding_ring_cost + second_ring_cost - first_ring_sale

    # Display Jim's total out of pocket expense
    result = total_cost
    return result

print(solution())