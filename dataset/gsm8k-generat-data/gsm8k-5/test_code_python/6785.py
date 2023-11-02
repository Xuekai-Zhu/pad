def solution():
    sweatshirt_cost = 15  # The cost of each sweatshirt is $15
    tshirt_cost = 10  # The cost of each T-shirt is $10
    num_sweatshirts = 3  # Hannah bought 3 sweatshirts
    num_tshirts = 2  # Hannah bought 2 T-shirts

    # Calculate the total cost of sweatshirts
    total_sweatshirt_cost = sweatshirt_cost * num_sweatshirts

    # Calculate the total cost of T-shirts
    total_tshirt_cost = tshirt_cost * num_tshirts

    # Calculate the total cost of all items
    total_cost = total_sweatshirt_cost + total_tshirt_cost
    result = total_cost
    return result

print(solution())