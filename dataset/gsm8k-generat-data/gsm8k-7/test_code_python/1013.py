def solution():
    num_longsleeve_jerseys = 4
    longsleeve_price = 15

    striped_price = 10

    total_spent = 80

    # Calculate the total cost of all long-sleeved jerseys
    total_longsleeve_cost = num_longsleeve_jerseys * longsleeve_price

    # Calculate the total cost of all striped jerseys
    total_striped_cost = total_spent - total_longsleeve_cost

    # Calculate the number of striped jerseys
    num_striped_jerseys = total_striped_cost / striped_price
    result = num_striped_jerseys
    return result

print(solution())