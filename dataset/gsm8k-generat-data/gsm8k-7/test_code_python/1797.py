def solution():
    num_tshirts = 3
    tshirt_price = 20
    pants_cost = 50

    # Calculate the total cost of all t-shirts
    total_tshirt_cost = num_tshirts * tshirt_price

    # Calculate the total cost of all items
    total_cost = total_tshirt_cost + pants_cost

    result = total_cost
    return result

print(solution())