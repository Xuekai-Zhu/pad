def solution():
    shirt_cost = 7  # A shirt costs $7
    shoe_cost = shirt_cost + 3  # A pair of shoes is $3 more than the shirt
    num_shirts = 2  # Sofia is buying 2 shirts
    bag_cost = (shirt_cost * num_shirts) / 2  # The bag costs half the total price of 2 shirts
    total_cost = (shirt_cost * num_shirts) + (shoe_cost) + (bag_cost)  # Calculate the total cost of all items
    result = total_cost
    return result

print(solution())