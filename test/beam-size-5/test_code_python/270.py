def solution():
    num_tomato_seeds = 20
    tomato_price = 40

    num_celery_seeds = 80
    celery_price = 30

    # Calculate the total cost of all tomato seeds
    total_tomato_cost = num_tomato_seeds * tomato_price

    # Calculate the total cost of all celery seeds
    total_celery_cost = num_celery_seeds * celery_price

    # Calculate the total cost of all seeds
    total_cost = total_tomato_cost + total_celery_cost
    result = total_cost
    return result

print(solution())