def solution():
    # Define the prices of cherries and olives
    cherry_price = 5
    olive_price = 7

    # Calculate the total cost before discount
    total_cost = (cherry_price + olive_price) * 50

    # Calculate the discount and apply it to the total cost
    discount = 0.1
    discounted_total_cost = total_cost * (1 - discount)

    result = discounted_total_cost
    return result

print(solution())