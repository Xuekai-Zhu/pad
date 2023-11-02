def solution():
    num_geckos = 3
    gecko_cost = 15

    num_iguanas = 2
    iguana_cost = 5

    num_snakes = 4
    snake_cost = 10

    months_per_year = 12

    # Calculate the total cost to feed all geckos for a year
    total_gecko_cost = num_geckos * gecko_cost * months_per_year

    # Calculate the total cost to feed all iguanas for a year
    total_iguana_cost = num_iguanas * iguana_cost * months_per_year

    # Calculate the total cost to feed all snakes for a year
    total_snake_cost = num_snakes * snake_cost * months_per_year

    # Calculate the total cost to feed all pets for a year
    total_cost = total_gecko_cost + total_iguana_cost + total_snake_cost
    result = total_cost
    return result

print(solution())