def solution():
    num_sweatshirts = 3
    sweatshirt_price = 15.0

    num_tshirts = 2
    tshirt_price = 10.0

    # Calculate the total cost of all sweatshirts
    total_sweatshirts_cost = num_sweatshirts * sweatshirt_price

    # Calculate the total cost of all t-shirts
    total_tshirts_cost = num_tshirts * tshirt_price

    # Calculate the total cost of all clothing items
    total_cost = total_sweatshirts_cost + total_tshirts_cost
    result = total_cost
    return result

print(solution())