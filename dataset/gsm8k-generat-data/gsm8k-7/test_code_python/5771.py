def solution():
    num_shirts = 10
    shirt_price = 6

    num_pants = num_shirts / 2
    pants_price = 8

    # Calculate the total cost of all shirts
    total_shirts_cost = num_shirts * shirt_price

    # Calculate the total cost of all pants
    total_pants_cost = num_pants * pants_price

    # Calculate the total cost of all items
    total_cost = total_shirts_cost + total_pants_cost
    result = total_cost
    return result

print(solution())