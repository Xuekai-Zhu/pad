def solution():
    
    # Define the number of people and the prices of the chicken and pasta salad
    num_people = 16
    chicken_price = 6.5
    pasta_price = 6

    # Calculate the total cost of the chicken salad
    chicken_cost = 10 * chicken_price

    # Calculate the total cost of the pasta salad
    pasta_cost = 6 * pasta_price

    # Calculate the total cost of the catering
    total_cost = chicken_cost + pasta_cost

    # return the result
    result = total_cost
    return result

print(solution())