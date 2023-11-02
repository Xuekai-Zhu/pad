def solution():
    """Harry owns 3 geckos, 2 iguanas, and 4 snakes. If he spends $10 to feed each snake, $5 to feed each iguana, and $15 to feed each gecko every month, how much does he spend every year to feed all his pets?"""
    # Define the number of geckos, iguanas, and snakes Harry owns
    num_geckos = 3
    num_iguanas = 2
    num_snakes = 4

    # Define the cost of feeding each type of pet per month
    gecko_cost = 15
    iguana_cost = 5
    snake_cost = 10

    # Calculate the monthly cost of feeding all the pets
    total_cost_per_month = (num_geckos * gecko_cost) + (num_iguanas * iguana_cost) + (num_snakes * snake_cost)

    # Calculate the annual cost of feeding all the pets
    total_cost_per_year = total_cost_per_month * 12

    # return the result
    result = total_cost_per_year
    return result

print(solution())