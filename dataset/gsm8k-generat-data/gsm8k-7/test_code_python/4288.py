def solution():
    num_hamburgers = 2
    hamburger_price = 5

    num_colas = 3
    cola_price = 2

    discount_coupon = 4

    # Calculate the total cost of all hamburgers
    total_hamburger_cost = num_hamburgers * hamburger_price

    # Calculate the total cost of all colas
    total_cola_cost = num_colas * cola_price

    # Calculate the total cost before discount
    total_cost_before_discount = total_hamburger_cost + total_cola_cost

    # Apply the discount coupon
    total_cost_after_discount = total_cost_before_discount - discount_coupon

    result = total_cost_after_discount
    return result

print(solution())