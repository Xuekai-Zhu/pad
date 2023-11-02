def solution():
    num_roses = 20
    num_lilies = (3/4) * num_roses
    rose_price = 5
    lily_price = 2 * rose_price

    # Calculate the cost of all roses
    total_rose_cost = num_roses * rose_price

    # Calculate the cost of all lilies
    total_lily_cost = num_lilies * lily_price

    # Calculate the total cost of all flowers
    total_cost = total_rose_cost + total_lily_cost
    result = total_cost
    return result

print(solution())