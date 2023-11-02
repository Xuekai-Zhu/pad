def solution():
    velvet_price = 24
    pattern_price = 15
    thread_price = 3
    num_threads = 2
    total_cost = 141

    # Calculate the total cost of the fabric
    fabric_cost = total_cost - pattern_price - (num_threads * thread_price)

    # Calculate the number of yards of fabric that Louis bought
    num_yards = fabric_cost / velvet_price
    result = num_yards
    return result

print(solution())