def solution():
    milkshakes_sold = 6
    milkshakes_price = 5.5

    burger_platters_sold = 9
    burger_platters_price = 11

    sodas_sold = 20
    sodas_price = 1.5

    # Calculate the total revenue from milkshakes
    milkshakes_revenue = milkshakes_sold * milkshakes_price

    # Calculate the total revenue from burger platters
    burger_platters_revenue = burger_platters_sold * burger_platters_price

    # Calculate the total revenue from sodas
    sodas_revenue = sodas_sold * sodas_price

    # Calculate the total revenue
    total_revenue = milkshakes_revenue + burger_platters_revenue + sodas_revenue
    result = total_revenue

print(solution())