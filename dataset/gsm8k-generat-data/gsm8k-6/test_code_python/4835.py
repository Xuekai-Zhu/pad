def solution():
    # Calculate the cost of the 2 shirts and a pair of shoes
    shirt_cost = 7
    shoe_cost = shirt_cost + 3
    total_cost = 2*shirt_cost + shoe_cost

    # Calculate the cost of the bag
    bag_cost = (2*shirt_cost + shoe_cost) / 2

    # Calculate the total cost of all items
    total_cost = total_cost + bag_cost
    result = total_cost
    return result

print(solution())