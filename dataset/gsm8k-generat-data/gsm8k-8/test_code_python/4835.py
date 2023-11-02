def solution():
    # Define the cost of a shirt and a pair of shoes
    shirt_cost = 7
    shoe_cost = shirt_cost + 3

    # Calculate the total cost of 2 shirts and a pair of shoes
    total_cost = 2 * shirt_cost + shoe_cost

    # Calculate the cost of the bag
    bag_cost = 0.5 * total_cost

    # Calculate the total cost of all items
    total_price = total_cost + bag_cost

    result = total_price
    return result

print(solution())