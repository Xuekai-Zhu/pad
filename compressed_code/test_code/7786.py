def solution():
    
    wedding_ring_price = 10000
    wife_ring_price = wedding_ring_price * 2
    sold_first_ring_price = wedding_ring_price / 2
    total_spent = wedding_ring_price + wife_ring_price - sold_first_ring_price
    result = total_spent
    return result

print(solution())