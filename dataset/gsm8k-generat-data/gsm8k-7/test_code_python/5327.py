def solution():
    original_jewelry_price = 30
    increased_jewelry_price = 40
    original_painting_price = 100
    increased_painting_price = original_painting_price * 1.2 # 20% increase

    num_jewelry = 2
    num_paintings = 5

    # Calculate the total cost of all jewelry at the increased price
    total_jewelry_cost = num_jewelry * increased_jewelry_price

    # Calculate the total cost of all paintings at the increased price
    total_paintings_cost = num_paintings * increased_painting_price

    # Calculate the total price the buyer would pay
    total_price = total_jewelry_cost + total_paintings_cost
    result = total_price
    return result

print(solution())