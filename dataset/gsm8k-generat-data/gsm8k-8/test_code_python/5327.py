def solution():
    # Define the original prices and the increased prices
    jewelry_original_price = 30
    jewelry_new_price = 40
    painting_original_price = 100
    painting_new_price = 120

    # Define the number of jewelry and paintings being bought
    num_jewelry = 2
    num_paintings = 5

    # Calculate the total cost of the purchase
    total_cost = num_jewelry * jewelry_new_price + num_paintings * painting_new_price
    result = total_cost
    return result

print(solution())