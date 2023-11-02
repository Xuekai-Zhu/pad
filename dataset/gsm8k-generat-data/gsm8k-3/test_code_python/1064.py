def solution():
    """Harry owns 3 geckos, 2 iguanas, and 4 snakes. If he spends $10 to feed each snake, $5 to feed each iguana, and $15 to feed each gecko every month, how much does he spend every year to feed all his pets?"""
    # Define the cost of feeding each type of pet per month
    GECKO_COST = 15
    IGUANA_COST = 5
    SNAKE_COST = 10

    # Define the number of each type of pet owned by Harry
    geckos = 3
    iguanas = 2
    snakes = 4

    # Calculate the total cost of feeding the geckos each month
    gecko_total = geckos * GECKO_COST * 12

    # Calculate the total cost of feeding the iguanas each month
    iguana_total = iguanas * IGUANA_COST * 12

    # Calculate the total cost of feeding the snakes each month
    snake_total = snakes * SNAKE_COST * 12

    # Calculate the total cost of feeding all the pets each month
    total_cost = gecko_total + iguana_total + snake_total

    # Display the total annual cost
    result = total_cost
    return result

print(solution())