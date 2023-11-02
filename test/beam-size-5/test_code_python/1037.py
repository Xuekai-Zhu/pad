def solution():
    num_people = 16
    chicken_salad_price = 6.5
    pasta_salad_price = 6.0
    num_chicken_salad = 10
    num_pasta_salad = 6

    # Calculate the total cost of all chicken salad
    total_chicken_cost = num_people * chicken_salad_price

    # Calculate the total cost of all pasta salad
    total_pasta_cost = num_people * pasta_salad_price

    # Calculate the total cost of all catering salad
    total_cost = total_chicken_cost + total_pasta_cost
    result = total_cost
    return result

print(solution())