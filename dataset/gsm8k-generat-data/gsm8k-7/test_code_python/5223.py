def solution():
    num_burgers = 30
    burger_price = 2

    num_fries = 12
    fries_price = 1.5

    # Calculate the total revenue from burgers
    burgers_revenue = num_burgers * burger_price

    # Calculate the total revenue from fries
    fries_revenue = num_fries * fries_price

    # Calculate the total revenue for the day
    total_revenue = burgers_revenue + fries_revenue
    result = total_revenue
    return result

print(solution())