def solution():
    original_necklaces = 10
    original_earrings = 15
    necklaces_bought = 10
    earrings_bought = 10 / 3 * 2
    earrings_received = 15 / 5 * 1
    total_necklaces = original_necklaces + necklaces_bought
    total_earrings = original_earrings + earrings_bought + earrings_received
    total_jewelry = total_necklaces + total_earrings
    result = total_jewelry
    return result

print(solution())