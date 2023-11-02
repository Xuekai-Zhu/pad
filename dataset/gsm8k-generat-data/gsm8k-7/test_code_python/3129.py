def solution():
    num_rose_bushes = 6
    rose_bush_price = 75
    num_others_bushes = 2
    aloe_price = 100

    # Calculate the total cost of all rose bushes
    total_rose_bushes_cost = num_rose_bushes * rose_bush_price

    # Calculate the cost of rose bushes for his friend
    friend_rose_bushes_cost = num_others_bushes * rose_bush_price

    # Calculate the total cost of all plants for him
    total_plants_cost = total_rose_bushes_cost + (2 * aloe_price) - friend_rose_bushes_cost
    result = total_plants_cost
    return result

print(solution())