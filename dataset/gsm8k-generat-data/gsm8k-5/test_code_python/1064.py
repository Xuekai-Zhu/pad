def solution():
    geckos = 3
    iguanas = 2
    snakes = 4
    snake_food_cost = 10
    iguana_food_cost = 5
    gecko_food_cost = 15

    # Calculate the total cost to feed all the snakes for a month
    total_snake_food_cost = snakes * snake_food_cost

    # Calculate the total cost to feed all the iguanas for a month
    total_iguana_food_cost = iguanas * iguana_food_cost

    # Calculate the total cost to feed all the geckos for a month
    total_gecko_food_cost = geckos * gecko_food_cost

    # Calculate the total cost to feed all the pets for a month
    total_monthly_cost = total_snake_food_cost + total_iguana_food_cost + total_gecko_food_cost

    # Calculate the total cost to feed all the pets for a year
    total_yearly_cost = total_monthly_cost * 12
    result = total_yearly_cost
    return result

print(solution())