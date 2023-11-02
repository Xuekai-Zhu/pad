def solution():
    tshirt_cost = 20
    pants_cost = 80
    shoes_cost = 150
    discount = 0.1

    num_tshirts = 4
    num_pants = 3
    num_shoes = 2

    # Calculate the total cost of all T-shirts
    total_tshirt_cost = num_tshirts * tshirt_cost

    # Calculate the total cost of all pants
    total_pants_cost = num_pants * pants_cost

    # Calculate the total cost of all shoes
    total_shoes_cost = num_shoes * shoes_cost

    # Calculate the total cost of all items before the discount
    total_cost_before_discount = total_tshirt_cost + total_pants_cost + total_shoes_cost

    # Calculate the total amount of discount
    total_discount = discount * total_cost_before_discount

    # Calculate the total cost of all items after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount

    result = total_cost_after_discount
    return result

print(solution())