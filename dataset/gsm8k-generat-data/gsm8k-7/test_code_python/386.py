def solution():
    original_shoe_price = 50
    num_shoes = 2
    original_dress_price = 100
    shoe_discount = 0.4
    dress_discount = 0.2

    # Calculate the discounted price of the shoes
    discounted_shoe_price = original_shoe_price * (1 - shoe_discount)
    total_shoe_cost = discounted_shoe_price * num_shoes

    # Calculate the discounted price of the dress
    discounted_dress_price = original_dress_price * (1 - dress_discount)

    # Calculate the total cost of all items
    total_cost = total_shoe_cost + discounted_dress_price
    result = total_cost
    return result

print(solution())