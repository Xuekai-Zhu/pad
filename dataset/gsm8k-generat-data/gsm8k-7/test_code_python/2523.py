def solution():
    jim_ring_cost = 10000
    wife_ring_cost = jim_ring_cost * 2
    first_ring_sales = jim_ring_cost / 2

    # Calculate Jim's total out of pocket cost
    total_cost = jim_ring_cost + wife_ring_cost - first_ring_sales
    result = total_cost
    return result

print(solution())